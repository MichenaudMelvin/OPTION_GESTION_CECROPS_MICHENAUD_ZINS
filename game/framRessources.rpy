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
        humainEnvoyes = renpy.input("Bien, entrez le nombre d'hommes que vous voulez envoyer : ", length=3)
        #besoin des expressions régulières / rationnelles pour éviter une erreur. see : https://www.w3schools.com/jsref/jsref_regexp_not_0-9.asp
        if not humainEnvoyes:
            humainEnvoyes = 0
        humainEnvoyes = int(humainEnvoyes)

    $ joueur.humainEpuises(humainEnvoyes)

    if(joueur.getHumainEpuises > joueur.getRessourceHumain):
        o "Vous n'avez pas assez d'Hommes pour tout récolez, veuillez réduire vos ambitions."
        $ joueur.humainEpuises(-humainEnvoyes)
        jump farm
    elif(joueur.getHumainEpuises == 0):
        o "Humm... vous n'avez envoyé personne..."
        jump farm
    
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