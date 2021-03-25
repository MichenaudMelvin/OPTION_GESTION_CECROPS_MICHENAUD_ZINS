define s = Character("Senateur")
define o = Character("Assistant")
define personne = Character("")

init python:
    import random
    
    #Pour chaque village
    class Village():
        def __init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain):
            self.__nomVillage = nomVillage #str / nom du village
            self.__ressourceBois = ressourceBois #int / ressources en bois du village
            self.__ressourcePierre = ressourcePierre #int / ressources en pierre du village
            self.__ressourceHumain = ressourceHumain #int / ressources humaines du village
        
        #@property pour ne pas mettre "()" après la méthode // permet l'affichage dans les dialogues
        @property
        def getNomVillage(self):
            return self.__nomVillage
        
        @property
        def getRessourceBois(self):
            return self.__ressourceBois
        
        @property
        def getRessourcePierre(self):
            return self.__ressourcePierre
       
        @property
        def getRessourceHumain(self):
            return self.__ressourceHumain
        
        #pour ajouter / enlever des ressources à un village
        def addRessources(self, bois, pierre, humain):
            self.__ressourceBois = self.__ressourceBois + bois
            self.__ressourcePierre = self.__ressourcePierre + pierre
            self.__ressourceHumain = self.__ressourceHumain + humain

        def renommer(self, nouveauNom):
            self.__nomVillage = nouveauNom
    
    #classe hérité de village
    class VillageJoueur(Village):
        def __init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain, humainEpuises, possibiliteFarm, niveauDiplomatie, debutJeu, manqueDeRessource, diplomatieDoneOnce):
            Village.__init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain)
            self.__nomVillage = nomVillage #str / nom du village
            self.__ressourceBois = ressourceBois #int / ressources en bois du village
            self.__ressourcePierre = ressourcePierre #int / ressources en pierre du village
            self.__ressourceHumain = ressourceHumain #int / ressources humaines/militaires du village
            self.__humainEpuises = humainEpuises #int / les ressources humaines envoyés après qu'ils ait fait une action
            self.__possibiliteFarm = possibiliteFarm #bool / si le joueur peut farm ou si il doit attendre / uniquement pour le joueur
            self.__niveauDiplomatie = niveauDiplomatie #int / niveau de diplomatie du joueur en fonctions des choix qu'ils peut faire dans #diplomatie.rpy / change l'issue d'un combat / varie entre 1 et -1 / default = 0
            self.__debutJeu = debutJeu #bool / si le joueur vient de commencer ou non / uniquement pour le joueur
            self.__manqueDeRessource = manqueDeRessource #bool / uniquement si le joueur n'a pas assez de joueur pour réaliser n'importe quelle action
            self.__diplomatieDoneOnce = diplomatieDoneOnce #bool / si le joueur est deja passé par le label diplomatie

        @property
        def getHumainEpuises(self):
            return self.__humainEpuises
        
        def getPossibiliteFarm(self):
            return self.__possibiliteFarm
        
        def getDebutJeu(self):
            return self.__debutJeu
        
        def avanceJeu(self):
            self.__debutJeu = False
        
        @property
        def getNiveauDiplomatie(self):
            return self.__niveauDiplomatie

        #pour le changement de niveau de diplomatie du joueur en fonction de ses choix
        def changeNiveauDiplomatie(self, nouvelleValeure):
            self.__niveauDiplomatie = self.__niveauDiplomatie + nouvelleValeure
            if(self.__niveauDiplomatie > 1):
                self.__niveauDiplomatie = 1
            elif(self.__niveauDiplomatie < -1):
                self.__niveauDiplomatie = -1
        
        def humainEpuises(self, nombreHumainsEnvoyes):
            self.__humainEpuises = self.__humainEpuises + nombreHumainsEnvoyes
        
        def possibiliteFarm(self, bool):
            self.__possibiliteFarm = bool
        
        def getManqueDeRessource(self):
            return self.__manqueDeRessource
        
        def conditionDeDefaiteParRessources(self):
            self.__manqueDeRessource = True
        
        def getDiplomatieDoneOnce(self):
            return self.__diplomatieDoneOnce
        
        def diplomatieAlreadyDoneOnce(self):
            self.__diplomatieDoneOnce = True
        
    #classe hérité de village
    class VillageEnnemi(Village):
        def __init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain, king, villageChoisi, defeatVillage, humainEnvoyesParVillageEnnemi):
            Village.__init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain)
            self.__nomVillage = nomVillage #str / nom du village
            self.__ressourceBois = ressourceBois #int / ressources en bois du village
            self.__ressourcePierre = ressourcePierre #int / ressources en pierre du village
            self.__ressourceHumain = ressourceHumain #int / ressources humaines du village
            self.__king = king #bool / si le village est maitre de l'île
            self.__defeatVillage = defeatVillage #bool / si le village a deja été vaincu par le joueur / default = False
            self.__humainEnvoyesParVillageEnnemi = humainEnvoyesParVillageEnnemi #int / nombre d'humains envoyé au combat par le village adverse / default = 0
        
        def getKing(self):
            return self.__king
        
        def getDefeatVillage(self):
            return self.__defeatVillage

        def defeatVillage(self, bool):
            self.__defeatVillage = bool
        
        @property
        def getHumainEnvoyesParVillageEnnemi(self):
            return self.__humainEnvoyesParVillageEnnemi

        #humains envoyés par le village ennemi = nombre aléatoire entre le nombre total d'humains du village village divisé par 2 et le nombre total d'humain du village
        def humainEnvoyesParVillageEnnemi(self):
            self.__humainEnvoyesParVillageEnnemi = random.randint(self.__ressourceHumain/2, self.__ressourceHumain)
            self.__ressourceHumain = self.__ressourceHumain - self.__humainEnvoyesParVillageEnnemi
            return self.__humainEnvoyesParVillageEnnemi
        
    class Batiment():
        def __init__(self, type, niveau):
            self.__type = type #str / type du batiment (caserne, mine, senat)
            self.__niveau = niveau #int / niveau du batiment, max = 3, debut = 1
        
        @property
        def getType(self):
            return self.__type
        
        @property
        def getNiveau(self):
            return self.__niveau

        def niveauSup(self):
            self.__niveau = self.__niveau + 1

#Pour la world map
screen conquete_map():
    imagemap:
        idle "map"
        hover "maphovered"

        hotspot (587, 150, 100, 63) action Jump("islesbury")
        hotspot (813, 209, 100, 63) action Jump("redwater")
        hotspot (818, 411, 99, 64) action Jump("swanford")
        hotspot (329, 456, 99, 63) action Jump("ourBase")
        #pose de la couronne au dessus du village maitre de l'ile
        if(islesbury.getKing() == True):
            add "king.png" xalign 0.496 yalign 0.14
        elif(redwater.getKing() == True):
            add "king.png" xalign 0.683 yalign 0.231
        elif(swanford.getKing() == True):
            add "king.png" xalign 0.687 yalign 0.52

label start:
    #ici definition de variable et des choses qui changeront pas trop
    $ nombre_guerrier = 0
    $ nombre_archer = 0
    $ nombre_cavalier = 0
    $ joueur = VillageJoueur("Lunaris", 200, 200, 100, 0, True, 0, True, False, False)
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
        $ islesbury = VillageEnnemi("Islesbury", renpy.random.randint(500, 700), renpy.random.randint(500, 700), renpy.random.randint(500, 700), True, False, False, 0)
        $ redwater = VillageEnnemi("Redwater", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
        $ swanford = VillageEnnemi("Swanford", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
    elif(king == 2):
        $ islesbury = VillageEnnemi("Islesbury", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
        $ redwater = VillageEnnemi("Redwater", renpy.random.randint(500, 700), renpy.random.randint(500, 700), renpy.random.randint(500, 700), True, False, False, 0)
        $ swanford = VillageEnnemi("Swanford", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
    elif(king == 3):
        $ islesbury = VillageEnnemi("Islesbury", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
        $ redwater = VillageEnnemi("Redwater", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
        $ swanford = VillageEnnemi("Swanford", renpy.random.randint(500, 700), renpy.random.randint(500, 700), renpy.random.randint(500, 700), True, False, False, 0)
    
    #creation des batiments
    $ caserne = Batiment("caserne", 1)
    $ mine = Batiment("mine", 1)
    $ senat = Batiment("senat", 1)
    
    scene villagesenateur
    with fade
    
    #affichage des pictogrammes
    show ressourcebois:
        xalign 0.005
        yalign 0.05
    show ressourcepierre:
        xalign 0.02
        yalign 0.3
    show pictoguerrier:
        xalign 0.02
        yalign 0.55
    show pictoepuises:
        xalign 0.02
        yalign 0.75
    
    #afficher les ressources du joueur
    show screen ressourceJoueur
    
    show senateur:
        xalign 0.5
        yalign 0.5
    s "Bonjour"
    show senateur:
        xalign 0.99
        yalign 0.5
    with move
    jump choix

label choix:
    #mise a zéro de toutes les ressources si elles sont négatives (juste au cas ou)
    if(joueur.getRessourceBois < 0):
        $ joueur.addRessources(-joueur.getRessourceBois, 0, 0)
    if(joueur.getRessourcePierre < 0):
        $ joueur.addRessources(0, -joueur.getRessourcePierre, 0)
    if(joueur.getRessourceHumain < 0):
        $ joueur.addRessources(0, 0, -joueur.getRessourceHumain)
    
    #condition de défaite si les ressources sont trop faibles, évite aussi de bloquer le joueur.
    if(joueur.getRessourceBois <= 0 and joueur.getRessourcePierre <= 0 and joueur.getRessourceHumain <= 0):
        $ joueur.conditionDeDefaiteParRessources()
        jump defaite
    else:
        show screen senat
        show screen arbre
        show screen arene
        o "Sélectionnez un bâtiment."
        jump choix

label victory:
    o "Bravo monsieur le sénateur, [joueur.getNomVillage] a réussi à devenir maître de l'île grâce à vous !"
    return

# if(villageChoisi.getKing() == True and joueur.getDebutJeu() == True):


label defaite:
    $ joueur.humainEpuises(-joueur.getHumainEpuises)
    $ joueur.addRessources(-joueur.getRessourceBois, -joueur.getRessourcePierre, -joueur.getRessourceHumain)
    if(joueur.getManqueDeRessource() == True):
        o "Monsieur le sénateur, nous n'avons plus assez de ressources pour continuer."
        return
    else:
        if(islesbury.getKing() == True):
            o "A force d'améliorer les batiments de [joueur.getNomVillage], cela a attirer les regards de [islesbury.getNomVillage]."
        elif(redwater.getKing() == True):
            o "A force d'améliorer les batiments de [joueur.getNomVillage], cela a attirer les regards de [redwater.getNomVillage]."
        elif(swanford.getKing() == True):
            o "A force d'améliorer les batiments de [joueur.getNomVillage], cela a attirer les regards de [swanford.getNomVillage]."
        o "Ils ont eu peur de nous, et nous ont attaqués par surprises"
        o "Ils ont pillés toutes nos ressources et tous nos hommes sont morts..."
        return

#permet d'afficher les ressources, se met constament à jour
screen ressourceJoueur:
    frame:
        xpos 0.14
        ypos 0.1
        text "[joueur.getRessourceBois]":
            size 30
    frame:
        xpos 0.14
        ypos 0.3
        text "[joueur.getRessourcePierre]":
            size 30
    frame:
        xpos 0.14
        ypos 0.5
        text "[joueur.getRessourceHumain]":
            size 30
    frame:
        xpos 0.14
        ypos 0.7
        text "[joueur.getHumainEpuises]":
            size 30
