# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene plaine
    $ nombre_guerrier = 0
    $ nombre_archer = 0
    $ nombre_cavalier = 0

label villageDuScenateur:
    hide eileen 
   
    screen troupes:
        frame:
            xpos 20
            ypos 20
            text "Guerrier(s) : [nombre_guerrier]":
                size 30
        frame:
            xpos 420
            ypos 20
            text "Archer(s) : [nombre_archer]":
                size 30
        frame:
            xpos 820
            ypos 20
            text "Cavalier(s) : [nombre_cavalier]":
                size 30

    show screen senat
    show screen arbre
    show screen leave  
    show screen arene
    show screen troupes
    call screen leave
    
label interieur_senat:
    menu:
        "Amelioration":
            jump upgrade_senat
        "Assistant":
            jump assistant

label interieur_arene:
    menu:
        "Entraîner des troupes":
            jump fighters_creation
        "Améliorer le bâtiment":
            jump upgrade_building
        "Ne rien faire":
            jump start

label arbre:
    menu:
        "Récupérer des ressources":
            jump ressource
        "Améliorer le batiment":
            jump upgrade_building
        "Ne rien faire":
            jump villageDuScenateur
    return

label upgrade_senat: 
    "Voulez-vous aggrandir le sénat ?"
    menu:
        "Améliorer":
            jump upgrade
        "Ne rien faire":
            jump villageDuScenateur
    return

label upgrade_building: 
    "Êtes-vous sûr de vouloir aggrandir ce bâtiment ?"
    menu:
        "Aggrandir":
            jump upgrade
        "Ne rien faire":
            jump villageDuScenateur
    return

label assistant:
    e "De quoi avez-vous besoin ?"
    jump villageDuScenateur
    return

label upgrade:
    "L'aggrandissement est effectué."
    jump villageDuScenateur
    return 

label ressource:
    "Vous avez récupérer les ressources."
    jump villageDuScenateur
    return 

label fighters_creation:
    "Quelles troupes voulez-vous entraîner ?"
    menu:
        "Guerrier":
            jump nbr_guerrier
        "Archer":
            jump nbr_archer
        "Cavalier":
            jump nbr_cavalier

label nbr_guerrier:
    $ fighters_nbr = renpy.input("Combien voulez-vous en entraîner ?", allow="0123456789", length=2)
    python:
        fighters_nbr = int(fighters_nbr)
    $ nombre_guerrier = fighters_nbr + nombre_guerrier

    if fighters_nbr == 0:
        "Vous n'avez pas formé de guerrier."
    if fighters_nbr == 1:
        "Vous avez formé [fighters_nbr] guerrier."
    if fighters_nbr > 1:
        "Vous avez formé [fighters_nbr] guerriers."

    jump villageDuScenateur

label nbr_archer:
    $ fighters_nbr = renpy.input("Combien voulez-vous en entraîner ?", allow="0123456789", length=2)
    python:
        fighters_nbr = int(fighters_nbr)
    $ nombre_archer = fighters_nbr + nombre_archer

    if fighters_nbr == "0":
        "Vous n'avez pas formé d'archer."
    if fighters_nbr == "1":
        "Vous avez formé [fighters_nbr] archer."
    if fighters_nbr > "1":
        "Vous avez formé [fighters_nbr] archers."

    jump villageDuScenateur

label nbr_cavalier:
    $ fighters_nbr = renpy.input("Combien voulez-vous en entraîner ?", allow="0123456789", length=2)
    python:
        fighters_nbr = int(fighters_nbr)
    $ nombre_cavalier = fighters_nbr + nombre_cavalier

    if fighters_nbr == "0":
        "Vous n'avez pas formé de cavalier."
    if fighters_nbr == "1":
        "Vous avez formé [fighters_nbr] cavalier."
    if fighters_nbr > "1":
        "Vous avez formé [fighters_nbr] cavaliers."

    jump villageDuScenateur

