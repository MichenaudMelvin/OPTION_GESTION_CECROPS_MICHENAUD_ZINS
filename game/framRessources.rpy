label framRessources:
    if(joueur.getPossibiliteFarm() == True):
        menu:
            s "Vous voulez vraiment farmez un peu de bois et de pierre ?"
            "Oui":
                jump farm
            "Non":
                jump choix
    else:
        o "Eumm... monsieur le sénateur, vos bucherons et mineurs sont épuisés, il serait préférable de les laisser se reposer quelques temps."
        jump choix

label farm:
    python:
        humainEnvoyes = renpy.input("Bien, entrez le nombre d'hommes que vous voulez envoyer : ", allow="0123456789", length=3)
        if not humainEnvoyes:
            humainEnvoyes = 0
        intHumainEnvoyes = int(humainEnvoyes)


    if(intHumainEnvoyes > joueur.getRessourceHumain):
        menu:
            o "Vous n'avez pas assez d'Hommes pour combatre, veuillez réduire vos ambitions."
            "faire autre chose":
                jump choix
            "recommencer":
                jump farm
    elif(intHumainEnvoyes == 0):
        menu:
            o "Humm... vous n'avez envoyé personne..."
            "faire autre chose":
                jump choix
            "recommencer":
                jump fram
    
    #entre 1 et 15 : alea entre 15 à 30
    #entre 16 et 50 : alea entre 50 à 100
    #entre 51 et 100 : alea entre 200 à 300
    #101+ : alea entre 350 à 500

    if(joueur.getHumainEpuises > 0 and joueur.getHumainEpuises <= 15):
        $ aleatoireBois = renpy.random.randint(15, 30)
        $ aleatoirePierre = renpy.random.randint(15, 30)

    elif(joueur.getHumainEpuises >= 16 and joueur.getHumainEpuises <= 50):
        $ aleatoireBois = renpy.random.randint(50, 100)
        $ aleatoirePierre = renpy.random.randint(50, 100)

    elif(joueur.getHumainEpuises >= 51 and joueur.getHumainEpuises <= 100):
        $ aleatoireBois = renpy.random.randint(200, 300)
        $ aleatoirePierre = renpy.random.randint(200, 300)

    elif(joueur.getHumainEpuises > 100):
        $ aleatoireBois = renpy.random.randint(350, 500)
        $ aleatoirePierre = renpy.random.randint(350, 500)
    else:
        o "Oops, une erreur est survenue, veuillez réessayer"
        jump framRessources

    $ joueur.possibiliteFarm(False)

    $ joueur.addRessources(aleatoireBois, aleatoirePierre, 0)
    pause 2
    s "Et voila c'est fini"
    hide text
    show text "[joueur.getRessourceBois]\n\n\n\n\n[joueur.getRessourcePierre]\n\n\n\n\n[joueur.getRessourceHumain]\n\n\n\n[joueur.getHumainEpuises]":
        xalign 0.14
        yalign 0.1
    s "On a recoltés [aleatoireBois] bois et [aleatoirePierre] pierre"
    s "Ce qui fait un total de [joueur.getRessourceBois] bois et [joueur.getRessourcePierre] pierre."
    s "[joueur.getHumainEpuises] hommes on besoin de se reposer."
    jump choix