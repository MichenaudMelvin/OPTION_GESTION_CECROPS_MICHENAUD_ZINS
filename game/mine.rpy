init python:
    choixMine = []
    #Menu qui permet de choisir les différentes actions possibles du jeu // repris du tuto renpy
    class TitreMine(object):
        def __init__(self, title):
            self.kind = "titre"
            self.title = title

            choixMine.append(self)

    class MenuMine(object):
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

            choixMine.append(self)

    TitreMine(_("Que faire ?"))
    MenuMine("ameliorerMine", _("Améliorer"))
    MenuMine("expedition", _("Lancer une expédition"))

screen menuMine(adj):
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
                for i in choixMine:
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

label menuMine:
    $ renpy.choice_for_skipping()
    call screen menuMine(adj=menu_adjustment)
    $ tutorial = _return
    if not tutorial:
        jump end
    
    call expression tutorial.label
    jump notDefindedYet

label ameliorerMine:
    if mine.getNiveau < 3:
        $ mine.niveauSup()
        $ cout = -10 * mine.getNiveau
        $ joueur.addRessources(cout, cout)
        hide text
        show text "[joueur.getRessourceBois]\n\n\n\n\n[joueur.getRessourcePierre]\n\n\n\n\n[joueur.getRessourceHumain]":
            xalign 0.14
            yalign 0.1
        o "Votre mine est maintenant niveau [mine.getNiveau]."
    else:
        o "Vous ne pouvez plus améliorer votre mine."
    jump menuMine

label expedition:
    if joueur.getPossibiliteFarm():
        $ joueur.possibiliteFarm(False)
        $ quantitePierre = renpy.random.randint(30,60)
        $ joueur.addRessources(0, quantitePierre)
        hide text
        show text "[joueur.getRessourceBois]\n\n\n\n\n[joueur.getRessourcePierre]\n\n\n\n\n[joueur.getRessourceHumain]":
            xalign 0.14
            yalign 0.1
        o "Cette expédition vous a rapporté [quantitePierre] de pierre."
    else:
        o "Vous ne pouvez pas lancer d'expédition pour le moment."
    jump menuMine