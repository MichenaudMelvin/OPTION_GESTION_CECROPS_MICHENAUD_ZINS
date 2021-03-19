define s = Character("Senateur")
define o = Character("Assistant")
define personne = Character("")

init python:
    import re
    import random
    # choix = []
    # #Menu qui permet de choisir les différentes actions possibles du jeu // repris du tuto renpy
    # class Titre(object):
    #     def __init__(self, title):
    #         self.kind = "titre"
    #         self.title = title

    #         choix.append(self)

    # class Menu(object):
    #     def __init__(self, label, title, move=True):
    #         self.kind = "choix"
    #         self.label = label
    #         self.title = title

    #         if move and (move != "after"):
    #             self.move_before = True
    #         else:
    #             self.move_before = False

    #         if move and (move != "before"):
    #             self.move_after = True
    #         else:
    #             self.move_after = False

    #         choix.append(self)
    
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
        
        def addRessources(self, bois, pierre, humain):
            self.__ressourceBois = self.__ressourceBois + bois
            self.__ressourcePierre = self.__ressourcePierre + pierre
            self.__ressourceHumain = self.__ressourceHumain + humain

        def renommer(self, nouveauNom):
            self.__nomVillage = nouveauNom
    
    #classe hérité de village
    class VillageJoueur(Village):
        def __init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain, humainEpuises, possibiliteFarm, niveauDiplomatie, debutJeu):
            Village.__init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain)
            self.__nomVillage = nomVillage #str / nom du village
            self.__ressourceBois = ressourceBois #int / ressources en bois du village
            self.__ressourcePierre = ressourcePierre #int / ressources en pierre du village
            self.__ressourceHumain = ressourceHumain #int / ressources humaines/militaires du village
            self.__humainEpuises = humainEpuises #int / les ressources humaines envoyés après qu'ils ait fait une action
            self.__possibiliteFarm = possibiliteFarm #bool / si le joueur peut farm ou si il doit attendre / uniquement pour le joueur
            self.__niveauDiplomatie = niveauDiplomatie #int / niveau de diplomatie du joueur en fonctions des choix qu'ils peut faire dans #diplomatie.rpy / change l'issue d'un combat / varie entre 1 et -1 / default = 0
            self.__debutJeu = debutJeu #bool / si le joueur vient de commencer ou non / uniquement pour le joueur
        
        @property
        def getHumainEpuises(self):
            return self.__humainEpuises
        
        def getPossibiliteFarm(self):
            return self.__possibiliteFarm
        
        def getDebutJeu(self):
            return self.__debutJeu
        
        @property
        def getNiveauDiplomatie(self):
            return self.__niveauDiplomatie

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
        
        def avanceJeu(self):
            self.__debutJeu = False
    
    #classe hérité de village
    class VillageEnnemi(Village):
        def __init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain, king, villageChoisi, defeatVillage, humainEnvoyesParVillegaeEnnemi):
            Village.__init__(self, nomVillage, ressourceBois, ressourcePierre, ressourceHumain)
            self.__nomVillage = nomVillage #str / nom du village
            self.__ressourceBois = ressourceBois #int / ressources en bois du village
            self.__ressourcePierre = ressourcePierre #int / ressources en pierre du village
            self.__ressourceHumain = ressourceHumain #int / ressources humaines du villag
            self.__king = king #bool / si le village est maitre de l'île
            self.__defeatVillage = defeatVillage #bool / si le village a deja été vaincu par le joueur / default = False
            self.__humainEnvoyesParVillegaeEnnemi = humainEnvoyesParVillegaeEnnemi #int / nombre d'humains envoyé au combat par le village adverse / default = 0
        
        def getKing(self):
            return self.__king
        
        def getDefeatVillage(self):
            return self.__defeatVillage

        def defeatVillage(self, bool):
            self.__defeatVillage = bool
        
        @property
        def getHumainEnvoyesParVillageEnnemi(self):
            return self.__humainEnvoyesParVillegaeEnnemi

        def humainEnvoyesParVillegaeEnnemi(self):
            self.__humainEnvoyesParVillegaeEnnemi = random.randint(self.__ressourceHumain/2, self.__ressourceHumain)
            self.__ressourceHumain = self.__ressourceHumain - self.__humainEnvoyesParVillegaeEnnemi
            return self.__humainEnvoyesParVillegaeEnnemi
        
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

#     Titre(_("Que faire ?"))

#     Menu("strategieMap", _("Attaquer"))
#     Menu("batiments", _("Construire"))
#     Menu("framRessources", _("Récolter"))
#     Menu("diplomatie", _("Régler les conflits internes"))

# default menu_adjustment = ui.adjustment()

# screen menuChoix(adj):
#     frame:
#         xsize 640
#         xalign .5
#         ysize 485
#         ypos 30
#         has side "c r b"
#         viewport:
#             yadjustment adj
#             mousewheel False
#             vbox:
#                 for i in choix:
#                     if i.kind == "choix":
#                         textbutton i.title:
#                             action Return(i)
#                             left_padding 20
#                             xfill True
#                     else:
#                         null height 10
#                         text i.title alt ""
#                         null height 5
#         bar adjustment adj style "vscrollbar"
#         textbutton _("Faire autre chose"):
#             xfill True
#             action Return(False)
#             top_margin 10

#Pour la world map
screen conquete_map():
    imagemap:
        idle "map"
        hover "maphovered"

        hotspot (587, 150, 100, 63) action Jump("islesbury")
        hotspot (813, 209, 100, 63) action Jump("redwater")
        hotspot (818, 411, 99, 64) action Jump("swanford")
        hotspot (329, 456, 99, 63) action Jump("ourBase")
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
    $ joueur = VillageJoueur("Lunaris", 200, 200, 100, 0, True, 0, True)
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
        #les valeurs aleatoires sont ptet trop élevés
        $ islesbury = VillageEnnemi("islesbury", renpy.random.randint(500, 700), renpy.random.randint(500, 700), renpy.random.randint(500, 700), True, False, False, 0)
        $ redwater = VillageEnnemi("redwater", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
        $ swanford = VillageEnnemi("swanford", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
    elif(king == 2):
        $ islesbury = VillageEnnemi("islesbury", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
        $ redwater = VillageEnnemi("redwater", renpy.random.randint(500, 700), renpy.random.randint(500, 700), renpy.random.randint(500, 700), True, False, False, 0)
        $ swanford = VillageEnnemi("swanford", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
    elif(king == 3):
        $ islesbury = VillageEnnemi("islesbury", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
        $ redwater = VillageEnnemi("redwater", renpy.random.randint(350, 500), renpy.random.randint(350, 500), renpy.random.randint(350, 500), False, False, False, 0)
        $ swanford = VillageEnnemi("swanford", renpy.random.randint(500, 700), renpy.random.randint(500, 700), renpy.random.randint(500, 700), True, False, False, 0)
    
    #creation des batiments
    $ caserne = Batiment("caserne", 1)
    $ mine = Batiment("mine", 1)
    $ senat = Batiment("senat", 1)
    
    scene villagesenateur
    with fade
    show ressourcebois:
        xalign 0.005
        yalign 0.05
    show ressourcepierre:
        xalign 0.02
        yalign 0.3
    #permet d'afficher les ressources, se met constament à jour
    show screen ressourceJoueur
    
    #les icones sont trop grandes
    #{outlinecolor=#000000}{/outlinecolor}
    show senateur:
        xalign 0.5
        yalign 1.0
    s "Bonjour"
    show senateur at right
    with move
    jump choix

label choix:
    # $ renpy.choice_for_skipping()
    # call screen menuChoix(adj=menu_adjustment)
    # $ tutorial = _return
    # if not tutorial:
    #     jump end
    
    # call expression tutorial.label from _call_expression
    show screen senat
    show screen arbre
    show screen leave
    show screen arene
    call screen leave

label victory:
    $ not tutorial
    s "wow, we won"
    return

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
