define s = Character("Senateur")
define o = Character("OtherRandomCharacter")
define personne = Character("")

init python:
    choix = []
    #Menu qui permet de choisir les différentes actions possibles du jeu // repris du tuto renpy
    class Titre(object):
        def __init__(self, title):
            self.kind = "titre"
            self.title = title

            choix.append(self)

    class Menu(object):
        def __init__(self, label, title, move=True):
            self.kind = "choix"
            self.label = label
            self.title = title

            if move and (move != "after"):
                self.move_before = True
            else:
                self.move_before = False

            if move and (move != "before"):
                self.move_after = True
            else:
                self.move_after = False

            choix.append(self)
    
    #Pour chaque village
    class Village():
        def __init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain):
            self.__nomVillage = nomVillage #str / nom du village
            self.__ressourceBois = ressourceBois #int / ressources en bois du village
            self.__ressourcePierre = ressourcePierre #int / ressources en pierre du village
            self.__ressourceHumain = ressourceHumain #int / ressources humaines du village
        
        #property pour ne pas mettre "()" après la méthode // permet l'affichage dans les dialogues
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
        
        def renommer(self, nouveauNom):
            self.__nomVillage = nouveauNom
    
    #classe hérité de village
    class VillageJoueur(Village):
        def __init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain, humainEpuises, possibiliteFarm, debutJeu):
            Village.__init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain)
            self.__nomVillage = nomVillage #str / nom du village
            self.__ressourceBois = ressourceBois #int / ressources en bois du village
            self.__ressourcePierre = ressourcePierre #int / ressources en pierre du village
            self.__ressourceHumain = ressourceHumain #int / ressources humaines du village
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
        
        def humainEpuises(self, nombreHumainsEnvoyes):
            self.__ressourceHumain = self.__ressourceHumain - nombreHumainsEnvoyes
            self.__humainEpuises = self.__humainEpuises + nombreHumainsEnvoyes
        
        def addRessources(self, bois, pierre):
            self.__ressourceBois = self.__ressourceBois + bois
            self.__ressourcePierre = self.__ressourcePierre + pierre
        
        def possibiliteFarm(self, bool):
            self.__possibiliteFarm = bool
        
        def avanceJeu(self):
            self.__debutJeu = False
    
    #classe hérité de village
    class VillageEnnemi(Village):
        def __init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain, king, villageChoisi):
            Village.__init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain)
            self.__nomVillage = nomVillage #str / nom du village
            self.__ressourceBois = ressourceBois #int / ressources en bois du village
            self.__ressourcePierre = ressourcePierre #int / ressources en pierre du village
            self.__ressourceHumain = ressourceHumain #int / ressources humaines du villag
            self.__king = king #bool / si le village est maitre de l'île / immpossible pour le village du joueur
        
        def getKing(self):
            return self.__king
    
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
    
    Titre(_("Que faire ?"))

    Menu("strategieMap", _("Attaquer"))
    Menu("notDefindedYet", _("Construire"))
    Menu("framRessources", _("Récolter"))
    Menu("diplomatie", _("Régler les conflits internes"))

default menu_adjustment = ui.adjustment()

screen menuChoix(adj):
    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30
        has side "c r b"
        viewport:
            yadjustment adj
            mousewheel False
            vbox:
                for i in choix:
                    if i.kind == "choix":
                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True
                    else:
                        null height 10
                        text i.title alt ""
                        null height 5
        bar adjustment adj style "vscrollbar"
        textbutton _("Faire autre chose"):
            xfill True
            action Return(False)
            top_margin 10

#Pour la world map
screen conquete_map():
    imagemap:
        idle "map"
        hover "maphovered"

        hotspot (587, 150, 100, 63) action Jump("islesbury")
        hotspot (813, 209, 100, 63) action Jump("redwater")
        hotspot (818, 411, 99, 64) action Jump("swanford")
        hotspot (329, 456, 99, 63) action Jump("ourBase")
        #afficher aussi quand les villages sont détruits
        if(islesbury.getKing() == True):
            add "king.png" xalign 0.496 yalign 0.14
        elif(redwater.getKing() == True):
            add "king.png" xalign 0.683 yalign 0.231
        elif(swanford.getKing() == True):
            add "king.png" xalign 0.687 yalign 0.52

label start:
    #ici definition de variable et des choses qui changeront pas trop
    $ joueur = VillageJoueur("Lunaris", 200, 200, 100, 0, True, True)
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
        $ islesbury = VillageEnnemi("islesbury", 200, 200, 100, True, False)
        $ redwater = VillageEnnemi("redwater", 200, 200, 100, False, False)
        $ swanford = VillageEnnemi("swanford", 200, 200, 100, False, False)
    elif(king == 2):
        $ islesbury = VillageEnnemi("islesbury", 200, 200, 100, False, False)
        $ redwater = VillageEnnemi("redwater", 200, 200, 100, True, False)
        $ swanford = VillageEnnemi("swanford", 200, 200, 100, False, False)
    elif(king == 3):
        $ islesbury = VillageEnnemi("islesbury", 200, 200, 100, False, False)
        $ redwater = VillageEnnemi("redwater", 200, 200, 100, False, False)
        $ swanford = VillageEnnemi("swanford", 200, 200, 100, True, False)
    
    #creation des batiments
    $ caserne = Batiment("caserne", 1)
    $ mine = Batiment("mine", 1)
    $ senat = Batiment("senat", 1)

    scene villageDuScenateur
    
    show senateur:
        xalign 0.5
        yalign 1.0
    
    show ressourcebois:
        xalign 0.005
        yalign 0.02
    show ressourcepierre:
        xalign 0.02
        yalign 0.25
    show text "[joueur.getRessourceBois]\n\n\n\n\n[joueur.getRessourcePierre]\n\n\n\n\n[joueur.getRessourceHumain]":
        xalign 0.14
        yalign 0.1
    
    #les icones sont trop grandes
    #{outlinecolor=#000000}{/outlinecolor}

    s "Pensez à ne pas coder sur la branche 'main' et a coder en pull request"
    s "Pour cela, allez sur github desktop --> curent branch --> new branch et nommer votre branch"
    s "Pour ce qui est de l'interface, en gros ça serait comme ça, avec le menu + map en haut à gauche"
    show senateur at right
    with move
    s "Avec moi à droite"
    jump choix

label choix:
    $ renpy.choice_for_skipping()
    call screen menuChoix(adj=menu_adjustment)
    $ tutorial = _return
    if not tutorial:
        jump end
    
    call expression tutorial.label from _call_expression
    jump choix

label notDefindedYet:
    s "pas encore défini"
    jump choix

label end:
    s "Je sias pas encore si ce boutton va servir"
    return