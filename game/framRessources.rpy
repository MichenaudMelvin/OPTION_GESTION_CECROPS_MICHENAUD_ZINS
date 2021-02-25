label framRessources:
    menu:
        s "Vous voulez vraiment farmez un peu de bois et de pierre ?"
        "Oui":
            s "Ok allons-y"
        "Non":
            jump start
    #$ possibiliteFarm = False
    $ aleatoireBois = renpy.random.randint(15, 30)
    $ aleatoirePierre = renpy.random.randint(15, 30)

    $ ressourceBois = ressourceBois + aleatoireBois
    $ ressourcePierre = ressourcePierre + aleatoirePierre
    pause 2
    s "Et voila c'est fini"
    s "On a recoltés [aleatoireBois] bois et [aleatoirePierre] pierre"
    s "Ce qui fait un total de [ressourceBois] bois et [ressourcePierre] pierre"
    jump framRessources