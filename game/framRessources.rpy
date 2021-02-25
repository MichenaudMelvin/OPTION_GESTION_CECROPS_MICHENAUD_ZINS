#Not working
label framRessources:
    if (possibiliteFarm == True):
        menu:
            s "Vous voulez vraiment farmez un peu de bois et de pierre ?"
            "Oui":
                jump farm
            "Non":
                jump jeu
    else:
        o "Eumm... monsieur le sénateur, vos bucherons et mineurs sont épuisés, il serait préférable de les laisser se reposer quelques temps"
        jump jeu

label farm:
    python:
        humainEnvoyes = renpy.input("Bien, entrez le nombre d'Hommes que vous voulez envoyer : ", length=3)
        if not humainEnvoyes:
            humainEnvoyes = 0
    
    #not working
    if (humainEnvoyes > ressourceHumain):
            o "Vous n'avez pas assez d'Hommes pour tout récolez, veuillez réduire vos ambitions"
            jump farm
    
    #entre 1 et 15 : alea entre 15 à 30
    #entre 16 et 50 : alea entre 50 à 100
    #entre 51 et 100 : alea entre 200 à 300
    #101+ : alea entre 350 à 500

    #not working
    if (humainEnvoyes > 0 or humainEnvoyes <= 15):
        s "1st [humainEnvoyes]"
        $ aleatoireBois = renpy.random.randint(15, 30)
        $ aleatoirePierre = renpy.random.randint(15, 30)

    if (humainEnvoyes >= 16 or humainEnvoyes <= 50):
        s "2nd"
        $ aleatoireBois = renpy.random.randint(50, 100)
        $ aleatoirePierre = renpy.random.randint(50, 100)

    elif (humainEnvoyes >= 51 or humainEnvoyes <= 100):
        s "3rd"
        $ aleatoireBois = renpy.random.randint(200, 300)
        $ aleatoirePierre = renpy.random.randint(200, 300)

    elif (humainEnvoyes > 100):
        s "4th"
        $ aleatoireBois = renpy.random.randint(350, 500)
        $ aleatoirePierre = renpy.random.randint(350, 500)
    else:
        o "Oops, une erreur est survenue, veuillez réessayer"
        jump framRessources

    $ possibiliteFarm = False

    $ ressourceBois = ressourceBois + aleatoireBois
    $ ressourcePierre = ressourcePierre + aleatoirePierre
    pause 2
    s "Et voila c'est fini"
    hide text
    show text "[ressourceBois]\n\n\n\n\n[ressourcePierre]\n\n\n\n\n[ressourceHumain]":
        xalign 0.14
        yalign 0.1
    s "On a recoltés [aleatoireBois] bois et [aleatoirePierre] pierre"
    s "Ce qui fait un total de [ressourceBois] bois et [ressourcePierre] pierre"
    jump strategieMap