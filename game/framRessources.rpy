label framRessources:
    if (possibiliteFarm == True):
        menu:
            s "Vous voulez vraiment farmez un peu de bois et de pierre ?"
            "Oui":
                s "Ok allons-y"
            "Non":
                jump jeu
    else:
        o "Eumm... monsieur le sénateur, vos bucherons et mineurs sont épuisés, il serait préférable de les laisser se reposer quelques temps"
        jump jeu
    $ possibiliteFarm = False
    $ aleatoireBois = renpy.random.randint(15, 30)
    $ aleatoirePierre = renpy.random.randint(15, 30)

    $ ressourceBois = ressourceBois + aleatoireBois
    $ ressourcePierre = ressourcePierre + aleatoirePierre
    pause 2
    s "Et voila c'est fini"
    hide text
    show text "[ressourceBois]\n\n\n\n\n[ressourcePierre]":
        xalign 0.14
        yalign 0.1
    s "On a recoltés [aleatoireBois] bois et [aleatoirePierre] pierre"
    s "Ce qui fait un total de [ressourceBois] bois et [ressourcePierre] pierre"
    jump framRessources