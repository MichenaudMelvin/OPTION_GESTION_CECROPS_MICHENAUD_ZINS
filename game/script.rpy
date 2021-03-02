define s = Character("Senateur")
define o = Character("OtherRandomCharacter")
define personne = Character("")

#Menu qui permet de choisir les différentes actions possibles du jeu // repris du tuto renpy
init python:
    choix = []
    class Titre(object):
        def __init__(self, title):
            self.kind = "section"
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

label start:
    scene bg room
    show senateur:
        xalign 0.5
        yalign 1.0
    s "Pensez à ne pas coder sur la branche 'main' et a coder en pull request"
    s "Pour cela, allez sur github desktop --> curent branch --> new branch et nommer votre branch"
    s "On s'occupera de merge les branch plus tard"
    s "Dans vos pull request évitez aussi d'envoyer vos 'errors.txt' et 'traceback.txt'"
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

label end:
    s "Je sias pas encore si ce boutton va servir"
    return