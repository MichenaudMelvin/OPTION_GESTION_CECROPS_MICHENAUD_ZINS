define s = Character("Senateur")
define o = Character("OtherRandomCharacter")

label start:
    $ ressourceBois = 200
    $ ressourcePierre = 200
    scene villageDuScenateur

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
        s "Tu voudrais plutot voir le fram de ressources alros ?"
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

        hotspot (605, 157, 62, 53) action Jump("islesbury")
        hotspot (834, 216, 58, 49) action Jump("redwater")
        hotspot (838, 418, 59, 49) action Jump("swanford")
        hotspot (349, 463, 62, 49) action Jump("ourBase")