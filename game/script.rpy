define s = Character("Senateur")
define o = Character("OtherRandomCharacter")

#pour gestion diplomatie :
#faire un générateur de situation ex : "un chien a accidentellement brulé l'écurie" / "un prince a mangé toutes les pommes"
#regarder comme reign fonctionne

label start:
    #ici definition de variable et des choses qui changeront pas trop
    $ ressourceBois = 200
    $ ressourcePierre = 200
    $ ressourceHumain = 100
    $ possibiliteFarm = True
    $ debutJeu = True #Juste pour un dialogue (Pour l'instant)

    $ king = renpy.random.randint(1, 3) #definition aléatoire de la cité maitre de l'île 1 = islesbury / 2 = redwater / 3 = swanford
    
    scene villageDuScenateur
    show ressourcebois:
        xalign 0.005
        yalign 0.02
    show ressourcepierre:
        xalign 0.02
        yalign 0.25
    #les icones sont trop grandes
    #{outlinecolor=#000000}{/outlinecolor}
    show text "[ressourceBois]\n\n\n\n\n[ressourcePierre]\n\n\n\n\n[ressourceHumain]":
        xalign 0.14
        yalign 0.1

label jeu:
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
        s "Tu voudrais plutot voir le fram de ressources alors ?"
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

        hotspot (587, 150, 100, 63) action Jump("islesbury")
        hotspot (813, 209, 100, 63) action Jump("redwater")
        hotspot (818, 411, 99, 64) action Jump("swanford")
        hotspot (329, 456, 99, 63) action Jump("ourBase")
        if(king == 1):
            #islesbury
            add "king.png" xalign 0.496 yalign 0.14
        elif(king == 2):
            #redwater
            add "king.png" xalign 0.683 yalign 0.231
        elif(king == 3):
            #swanford
            add "king.png" xalign 0.687 yalign 0.52