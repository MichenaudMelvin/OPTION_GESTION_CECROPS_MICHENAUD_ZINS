define s = Character("Senateur")


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

    show senateur at left
    with move
    
    s "Et le sénateur à gauche"

    show senateur at right
    with move

    s "Ou l'inverse, le sénateur à droite et le menu + map en haut à droite"

    return