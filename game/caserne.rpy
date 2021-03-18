init python:
    choixCaserne = []
    #Menu qui permet de choisir les différentes actions possibles du jeu // repris du tuto renpy
    class TitreCaserne(object):
        def __init__(self, title):
            self.kind = "titre"
            self.title = title

            choixCaserne.append(self)

    class MenuCaserne(object):
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

            choixCaserne.append(self)

    TitreCaserne(_("Que faire ?"))
    MenuCaserne("ameliorerCaserne", _("Améliorer"))
    MenuCaserne("creerUnite", _("Créer une unité"))

screen menuCaserne(adj):
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
                for i in choixCaserne:
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

label ameliorerCaserne:
    if caserne.getNiveau < 3:
        $ caserne.niveauSup()
        $ cout = -10 * caserne.getNiveau
        $ joueur.addRessources(cout, cout)
        o "Votre caserne est maintenant niveau [caserne.getNiveau]."
    else:
        o "Vous ne pouvez plus améliorer votre caserne."

label creerUnite:
    $ joueur.addUnite(1)
    $ joueur.addRessources(-5, -8)
    o "Vous possédez maintenant [joueur.getRessourceUnite()] unités."