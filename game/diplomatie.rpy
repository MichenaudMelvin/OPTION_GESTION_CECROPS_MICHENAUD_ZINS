label diplomatie:
    show otherGuy:
        xalign -0.5
    with move
    show otherGuy at left
    with move
    o "Bonjour monsieur le sénateur"
    s "Bonjour"
    $ listeVille = ["Islesbur", "Redwater", "Swanford"]
    $ villeAlea = listeVille[renpy.random.randint(0, 2)]

    $ listePerso = ["Un prêtre", "Un chevalier", "Le marquis", "L'écuyer", "Un paysant", "La marquise", "Le prince", "Un chien", "Un cochon", "Un cheval", "Les innondations", "Les intempéries", "Le vent"]
    #De 0 à 6 : personnages humains / De 7 à 9 : annimaux / De 10 à 12 : météo // longueur : 12

    $ listeAction = ["a volé(e)", "a tué(e)", "a brulé", "a perdu", "s'est endormi", "a donné(e) de quoi manger à une famille fauchée", "a aidé(e) un paysant à récolter le blé", "a entraîné les soldats", "a vaincu un village ennemi"] #, "a sali", "", "a grandement aidé pendant une bataille contre [villeAlea]"]
    #Pour humains : De 0 à 2 : Negatif / De 3 à 4 : neutre / De 5 à 8 : positif // Pour annimaux : De 9 à  X : Negatif

    $ listeContextuelle = ["une épée", "de l'argent", "un", "un cusinier", "une clé", ""]
    #Pour humains // vol : De 0 à 2 : Negatif / 

    $ i = 0
    while i != 5:
        $ persoAlea = listePerso[renpy.random.randint(0, 12)]
        if (persoAlea == "Un prêtre" or persoAlea == "Un chevalier" or persoAlea == "Le marquis" or persoAlea == "L'écuyer" or persoAlea == "Un paysant" or persoAlea == "La marquise" or persoAlea == "Le prince"):
            s 'balgour'
            #Humains
            if (persoAlea == "Un chevalier" or persoAlea == "Le prince"):
                $ actionAlea = listeAction[renpy.random.randint(0, 8)]
            elif (persoAlea != "Un paysant"):
                $ actionAlea = listeAction[renpy.random.randint(0, 6)]
            else:
                $ actionAlea = listeAction[renpy.random.randint(0, 5)]
            if (actionAlea == "a volé(e)"):
                s 'balgour'
        elif (persoAlea == "Un chien" or persoAlea == "Un cochon" or persoAlea == "Un cheval"):
            #Annimaux
        
        elif (persoAlea == "Les innondations" or persoAlea == "Les intempéries" or persoAlea == "Le vent"):
            #Méteo
        
        else:
            #En cas d'erreur
            $ i = 5
            o "humm, ce n'est pas censé arriver"
            o "Réessayez s'il vous plaît"

            













        o "[persoAlea] [actionAlea] [objectAlea] [lieuAlea]"
        menu:
            personne "Que faire ?"
            "[choix1]":
                $ i = i + 1
            "[choix2]":
                $ i = i + 1