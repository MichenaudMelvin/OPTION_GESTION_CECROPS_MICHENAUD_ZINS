define s = Character("Senateur")
define o = Character("OtherRandomCharacter")

init python:
    tutorials = [ ]

    class Section(object):
        def __init__(self, title):
            self.kind = "section"
            self.title = title

            tutorials.append(self)


    class Tutorial(object):
        def __init__(self, label, title, move=True):
            self.kind = "tutorial"
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

            tutorials.append(self)


    Section(_("Quickstart"))

    Tutorial("alloooo", _("Player Experience"))
    Tutorial("tutorial_create", _("Creating a New Game"))
    Tutorial("tutorial_dialogue", _("Writing Dialogue"))
    Tutorial("tutorial_images", _("Adding Images"))
    Tutorial("tutorial_simple_positions", _("Positioning Images"))
    Tutorial("tutorial_transitions", _("Transitions"))
    Tutorial("tutorial_music", _("Music and Sound Effects"))
    Tutorial("tutorial_menus", _("Choices and Python"))
    Tutorial("tutorial_input", _("Input and Interpolation"))
    Tutorial("tutorial_video", _("Video Playback"))
    Tutorial("tutorial_nvlmode", _("NVL Mode"), move=None)
    Tutorial("director", _("Tools and the Interactive Director"))
    Tutorial("distribute", _("Building Distributions"))

    Section(_("In Depth"))

    Tutorial("text", _("Text Tags, Escapes, and Interpolation"))
    Tutorial("demo_character", _("Character Objects"))
    Tutorial("simple_displayables", _("Simple Displayables"), move=None)
    Tutorial("demo_transitions", _("Transition Gallery"))

    # Positions and Transforms?
    Tutorial("tutorial_positions", _("Position Properties"))

    # Advanced Transforms?
    Tutorial("tutorial_atl", _("Transforms and Animation"))
    Tutorial("transform_properties", _("Transform Properties"))

    Tutorial("new_gui", _("GUI Customization"))
    Tutorial("styles", _("Styles and Style Properties"), move=None)
    Tutorial("tutorial_screens", _("Screen Basics"), move=None)
    Tutorial("screen_displayables", _("Screen Displayables"), move=None)

    Tutorial("demo_minigame", _("Minigames and CDDs"))
    Tutorial("translations", _("Translations"))

default tutorials_adjustment = ui.adjustment()

screen tutorials(adj):

    frame:
        xsize 640
        xalign .5
        ysize 485
        ypos 30

        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
                for i in tutorials:

                    if i.kind == "tutorial":

                        textbutton i.title:
                            action Return(i)
                            left_padding 20
                            xfill True

                    else:

                        null height 10
                        text i.title alt ""
                        null height 5




        bar adjustment adj style "vscrollbar"

        textbutton _("That's enough for now."):
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
    show senateur happy at left
    with move

    $ renpy.choice_for_skipping()

    call screen tutorials(adj=tutorials_adjustment)

    $ tutorial = _return

    if not tutorial:
        jump end

    if tutorial.move_before:
        show senateur happy at center
        with move

    $ reset_example()

    call expression tutorial.label from _call_expression

    if tutorial.move_after:
        hide example
        show senateur happy at left
        with move

    jump tutorials

label end:

    show senateur happy at center
    with move

    show _finale behind senateur


    s "Thank you for viewing this tutorial."
    return

label alloooo:
    s "ça marche"