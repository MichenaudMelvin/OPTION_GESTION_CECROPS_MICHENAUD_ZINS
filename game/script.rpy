define s = Character("Senateur")
define o = Character("OtherRandomCharacter")
define personne = Character("")

#pour gestion diplomatie :
#faire un générateur de situation ex : "un chien a accidentellement brulé l'écurie" / "un prince a mangé toutes les pommes"
#regarder comme reign fonctionne

label start:
    #ici definition de variable et des choses qui changeront pas trop
    $ joueur = Village("Lunaris", 200, 200, 100, 0, True, True, False, False)
    python:
        nouveauNomVillage = renpy.input("Entrez le nom de votre village (10 caractères max) : ", length=10)
        if not nouveauNomVillage:
            nouveauNomVillage = "Lunaris"
    menu:
        personne 'Le nom de votre village sera "[nouveauNomVillage]", ça vous va ?'
        "C'est parfait !":
            $ joueur.renommer(nouveauNomVillage)
        "Changer de nom":
            jump start
    
    $ king = renpy.random.randint(1, 3) #definition aléatoire de la cité maitre de l'île 1 = islesbury / 2 = redwater / 3 = swanford
    if(king == 1):
        #mettre valeurs aléatoire pour chaque truc
        $ islesbur = Village("islesbur", 200, 200, 100, 0, False, False, True, False)
        $ redwater = Village("redwater", 200, 200, 100, 0, False, False, False, False)
        $ swanford = Village("swanford", 200, 200, 100, 0, False, False, False, False)
    elif(king == 2):
        $ islesbur = Village("islesbur", 200, 200, 100, 0, False, False, False, False)
        $ redwater = Village("redwater", 200, 200, 100, 0, False, False, True, False)
        $ swanford = Village("swanford", 200, 200, 100, 0, False, False, False, False)
    elif(king == 3):
        $ islesbur = Village("islesbur", 200, 200, 100, 0, False, False, False, False)
        $ redwater = Village("redwater", 200, 200, 100, 0, False, False, False, False)
        $ swanford = Village("swanford", 200, 200, 100, 0, False, False, True, False)
    
    scene villageDuScenateur
    show ressourcebois:
        xalign 0.005
        yalign 0.02
    show ressourcepierre:
        xalign 0.02
        yalign 0.25
    #les icones sont trop grandes
    #{outlinecolor=#000000}{/outlinecolor}

    #currently not working
    show text "[joueur.getRessourceBois]\n\n\n\n\n[joueur.getRessourcePierre]\n\n\n\n\n[joueur.getRessourceHumain]":
        xalign 0.14
        yalign 0.1

label jeu:
    show senateur:
        xalign 0.5
        yalign 1.0
    
    s "Pensez à ne pas coder sur la branche 'main' et a coder en pull request"

    s "Pour cela, allez sur github desktop --> curent branch --> new branch et nommer votre branch"

    s "On s'occupera de merge les branch plus tard"

    s "Dans vos pull request évitez aussi d'envoyer vos 'errors.txt' et 'traceback.txt'"
    
    s "Pour ce qui est de l'interface, en gros ça serait comme ça, avec le menu + map en haut à gauche"

    show senateur at left
    with move
    s "Et le sénateur à gauche"

    show senateur at right
    with move

    s "Ou l'inverse, le sénateur à droite et le menu + map en haut à droite"
    menu:
        s "Tu veux que je te montre la map ?"
        "Oui":
            hide senateur
            jump strategieMap
        "Non":
            s "Ok"
    
    menu:
        s "Tu voudrais plutot voir le fram de ressources alors ?"
        "Oui":
            jump framRessources
        "Non":
            s "Ok, a bientot alors"
    return

#Pour la world map
screen conquete_map():
    imagemap:
        idle "map"
        hover "maphovered"

        hotspot (587, 150, 100, 63) action Jump("islesbury")
        hotspot (813, 209, 100, 63) action Jump("redwater")
        hotspot (818, 411, 99, 64) action Jump("swanford")
        hotspot (329, 456, 99, 63) action Jump("ourBase")
        if(islesbury.getKing == True):
            #islesbury
            add "king.png" xalign 0.496 yalign 0.14
        elif(redwater.getKing == True):
            #redwater
            add "king.png" xalign 0.683 yalign 0.231
        elif(swanford.getKing == True):
            #swanford
            add "king.png" xalign 0.687 yalign 0.52

#Pour chaque village
init python:
    class Village():
        def __init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain):
            self.__nomVillage = nomVillage #str / nom du village
            self.__ressourceBois = ressourceBois #int / ressources en bois du village
            self.__ressourcePierre = ressourcePierre #int / ressources en pierre du village
            self.__ressourceHumain = ressourceHumain #int / ressources humaines du village
        
        @property
        def getNomVillage(self):
            return self.__nomVillage
        def getRessourceBois(self):
            return self.__ressourceBois
        def getRessourcePierre(self):
            return self.__ressourcePierre
        def getRessourceHumain(self):
            return self.__ressourceHumain
        def renommer(self, nouveauNom):
            self.__nomVillage = nouveauNom
    
    class VillageJoueur(Village):
        def __init__(self, humainEpuises, possibiliteFarm, debutJeu):
            Village.__init__(self)
            self.__humainEpuises = humainEpuises #int / les ressources humaines envoyés après qu'ils ait fait une action
            self.__possibiliteFarm = possibiliteFarm #bool / si le joueur peut farm ou si il doit attendre / uniquement pour le joueur
            self.__debutJeu = debutJeu #bool / si le joueur vient de commencer ou non / uniquement pour le joueur
        
        @property
        def getHumainEpuises(self):
            return self.__humainEpuises
        def getPossibiliteFarm(self):
            return self.__possibiliteFarm
        def getDebutJeu(self):
            return self.__debutJeu
        def possibiliteFarm(self, bool):
            self.__possibiliteFarm == bool

    class VillageEnnemi(Village):
        def __init__(self, king, villageChoisi):
            Village.__init__(self)
            self.__king = king #bool / si le village est maitre de l'île / immpossible pour le village du joueur
            self.__villageChoisi = villageChoisi #bool / avant une attaque, pour savoir quel village est selectionné
        
        @property
        def getKing(self):
            return self.__king
        def getVillageChoisi(self):
            return self.__villageChoisi
        def choixVillage(self, bool):
            self.__villageChoisi == bool