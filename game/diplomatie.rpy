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

    $ listeContextuelle = [" une épée", " de l'argent", " du pain", " un des cuisiners", " un des chevaux du roi", " un traitre", " les récoles de blé", " une partie des écuries", " l'entièreté de la forêt", " plusieurs armes de différents soldats", " les clés de la prison", " durant un combat", " dans la forêt", " pour mieux se préparer à un combat"]
    #Pour humains //// voler : De 0 à 1 : Negatif / 2 : neutre // tuer : De 3 à 4 : négatif / 5 : positif // bruler : De 6 à 8 : négatif // perdu : 9 : négatif / 10 neutre // endormi : 11 : negatif / 12 : neutre / 13 : positif //

    $ i = 0
    while i != 5:
        $ persoAlea = listePerso[renpy.random.randint(0, 12)]
        if(persoAlea == "Un prêtre" or persoAlea == "Un chevalier" or persoAlea == "Le marquis" or persoAlea == "L'écuyer" or persoAlea == "Un paysant" or persoAlea == "La marquise" or persoAlea == "Le prince"):
            #Pour humains
            if(persoAlea == "Un chevalier" or persoAlea == "Le prince"):
                $ actionAlea = listeAction[renpy.random.randint(0, 8)]
            elif(persoAlea != "Un paysant"):
                $ actionAlea = listeAction[renpy.random.randint(0, 6)]
            else:
                $ actionAlea = listeAction[renpy.random.randint(0, 5)]
            
            if(actionAlea == "a volé(e)"):
                $ contextAlea = listeContextuelle[renpy.random.randint(0, 2)]
                if(contextAlea == " une épée"):
                    $ choix1 = "Nous avons besoin d'armes"
                    $ choix2 = "Nous avons suffisament d'armes"
                elif(contextAlea == " de l'argent"):
                    $ choix1 = "L'argent est bien trop important"
                    $ choix2 = "Nous avons assez d'argent"
                elif(contextAlea == " du pain"):
                    $ choix1 = "La nourriture est une denré précieuse"
                    $ choix2 = "Ne me déranger pas pour si peu"
            
            elif(actionAlea == "a tué(e)"):
                $ contextAlea = listeContextuelle[renpy.random.randint(3, 5)]
                if(contextAlea == " un des cuisiners"):
                    $ choix1 = "Il y a d'autes cuistots"
                    $ choix2 = "Arrêter le coupable"
                elif(contextAlea == " un des chevaux du roi"):
                    $ choix1 = "C'est un crime impardonable"
                    $ choix2 = "Il y a des dizaines de chevaux"
                elif(contextAlea == " un traitre"):
                    $ choix1 = "Il aurait mieux valu le juger"
                    $ choix2 = "Féliciter"
            
            elif(actionAlea == "a brulé"):
                $ contextAlea = listeContextuelle[renpy.random.randint(6, 8)]
                if(contextAlea == " les récoles de blé"):
                    $ choix1 = "L'enfermer"
                    $ choix2 = "Ne rien faire"
                elif(contextAlea == " une partie des écuries"):
                    $ choix1 = ""
                    $ choix2 = ""
                elif(contextAlea == " l'entièreté de la forêt"):
                    $ choix1 = ""
                    $ choix2 = ""
            
            elif(actionAlea == "a perdu"):
                $ contextAlea = listeContextuelle[renpy.random.randint(9, 10)]
                if(contextAlea == " plusieurs armes de différents soldats"):
                    $ choix1 = ""
                    $ choix2 = ""
                elif(contextAlea == " les clés de la prison"):
                    $ choix1 = ""
                    $ choix2 = ""
            
            elif(actionAlea == "s'est endormi"):
                $ contextAlea = listeContextuelle[renpy.random.randint(11, 13)]
                if(contextAlea == " durant un combat"):
                    $ choix1 = ""
                    $ choix2 = ""
                elif(contextAlea == " dans la forêt"):
                    $ choix1 = ""
                    $ choix2 = ""
                elif(contextAlea == " pour mieux se préparer à un combat"):
                    $ choix1 = "Pas de fainéants dans les rangs de l'armée"
                    $ choix2 = "Il a bien raison de se reposer"
            
            elif(actionAlea == "a donné(e) de quoi manger à une famille fauchée"):
                $ contextAlea = ""
                $ choix1 = ""
                $ choix2 = ""
            
            elif(actionAlea == "a aidé(e) un paysant à récolter le blé"):
                $ contextAlea = ""
                $ choix1 = ""
                $ choix2 = ""
            
            elif(actionAlea == "a entraîné les soldats"):
                $ contextAlea = ""
                $ choix1 = "Féliciter"
                $ choix2 = "Dire qu'ils ne sont pas assez entrainés"
            
            elif(actionAlea == "a vaincu un village ennemi"):
                $ contextAlea = ""
                $ choix1 = "Faire une cérémonie pour célébrer cette victoire"
                $ choix2 = "Ne rien faire"
        # elif(persoAlea == "Un chien" or persoAlea == "Un cochon" or persoAlea == "Un cheval"):
        #     #Annimaux
        
        # elif(persoAlea == "Les innondations" or persoAlea == "Les intempéries" or persoAlea == "Le vent"):
        #     #Méteo
        
        else:
            #En cas d'erreur
            $ i = 4
            o "humm, ce n'est pas censé arriver, nom du perso choisi aléatoirement : [persoAlea]"
            o "Réessayez s'il vous plaît"
            $ persoAlea = "Réessayer"
            $ actionAlea = "Réessayer"
            $ contextAlea = " Réessayer"
            $ choix1 = "Réessayer"
            $ choix2 = "Réessayer"

            













        menu:
            o "[persoAlea] [actionAlea][contextAlea]. Que décidez vous de faire ?"
            "[choix1]":
                $ choixDuJoueur = choix1
                $ i = i + 1
                #add stats
            "[choix2]":
                $ choixDuJoueur = choix2
                $ i = i + 1
                #add stats
        
        #Un message différent pour chaque choix
        if(persoAlea == "Un prêtre" or persoAlea == "Un chevalier" or persoAlea == "Le marquis" or persoAlea == "L'écuyer" or persoAlea == "Un paysant" or persoAlea == "La marquise" or persoAlea == "Le prince"):
            #Pour humains
            #Pour voler :
            if(actionAlea == "a volé(e)"):
                if(choixDuJoueur == "Nous avons besoin de ces armes, retrouvez cette personne"):
                    messageSenateur = "Nous n'avons pas assez d'armes pour chaque soldats, mettez cette personne en prison."
                
                elif(choixDuJoueur == "Nous avons suffisament d'armes"):
                    messageSenateur = "Pas besoin de rechercher cette personne, nous avons largement assez d'armes pour tout le monde."
                
                elif(choixDuJoueur == "L'argent est bien trop important"):
                    messageSenateur = "Retrouvez-moi cet argent, nous en avons bien besoin pour pouvoir règner en maintre sur cet île."
                
                elif(choixDuJoueur == "Nous avons assez d'argent"):
                    messageSenateur "Nous avons suffisament d'argent pour tenir jusqu'au prochaines conquêtes."
                
                elif(choixDuJoueur == "La nourriture est une denré précieuse"):
                    messageSenateur = "Nous avons besoin de toute nourriture, comdaner ce vol."
                
                elif(choixDuJoueur == "Ne me déranger pas pour un morceau de pain"):
                    messageSenateur = "Ce n'est qu'un bout de pain, restez sérieux."
            
            #Pour tuer
            elif(actionAlea == "a tué(e)"):
                if(choixDuJoueur == "Il y a d'autes cuistots"):
                    messageSenateur = "Tant pis, il y a bien d'autres cuisinier au royaume."
                
                elif(choixDuJoueur == "Arrêter le coupable"):
                    messageSenateur = "Arrêter cette personne !"

                elif(choixDuJoueur == "C'est un crime impardonable"):
                    messageSenateur = "Veuillez executer le coupable, voler le cheval du roi est un crime impardonable."
                
                elif(choixDuJoueur == "Il y a des dizaines de chevaux"):
                    messageSenateur = "Il y a des dizaines de chevaux dans les écuries, le roi peut bien en prendre un autre."
                
                elif(choixDuJoueur == "Il aurait mieux valu le juger"):
                    messageSenateur = "Il aurait été préférable de le juger avant de le tuer."
                
                elif(choixDuJoueur == "Féliciter"):
                    messageSenateur = "Bien, vous lui transmettrais mes félicitations."
            
            #Pour bruler
            elif(actionAlea == "a brulé"):
                if(choixDuJoueur == ""):
                
                elif(choixDuJoueur == ""):
            
            #Pour perdu
            elif(actionAlea == "a perdu"):
                if(choixDuJoueur == ""):
                
                elif(choixDuJoueur == ""):
            
            #Pour endormi
            elif(actionAlea == "s'est endormi"):
                if(choixDuJoueur == ""):
                
                elif(choixDuJoueur == ""):







        s "[messageSenateur]"