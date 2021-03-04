label diplomatie:
    show otherGuy:
        xalign -0.5
    with move
    show otherGuy at left
    with move
    o "Bonjour monsieur le sénateur"
    s "Bonjour"
    $ listeVille = ["Islesbur", "Redwater", "Swanford"]

    $ listePerso = ["Un prêtre", "Un chevalier", "Le marquis", "L'écuyer", "Un paysant", "La marquise", "Le prince", "Un chien", "Un cochon", "Un cheval", "Les innondations", "Les intempéries", "Le vent"]
    #De 0 à 6 : personnages humains / De 7 à 9 : annimaux / De 10 à 12 : météo // longueur : 12

    $ autrePersoAlea = listePerso[renpy.random.randint(0, 9)] #juste pour fait s'envoler [autrePersoAlea]
    $ listeAction = ["a volé(e)", "a tué(e)", "a brulé", "a perdu", "s'est endormi", "a donné(e) de quoi manger à une famille fauchée", "a aidé(e) un paysant à récolter le blé", "a entraîné les soldats", "a vaincu un village ennemi", "a sali", "a dévoré", "a grandement aidé pendant une bataille contre [villeAlea]", "ont engloutis", "rendent le sol glissant", "fait tomber des troncs d'abres sur", "fait s'envoler [autrePersoAlea]"] #faire un systeme pour autrePersoAlea et villeAlea
    #Pour humains : De 0 à 2 : Negatif / De 3 à 4 : neutre / De 5 à 8 : positif // Pour annimaux : De 9 à 10 : Negatif / 11 : positif // Pour météo : 12 à 15 // longueur : 15

    $ listeContextuelle = [" une épée", " de l'argent", " du pain", " un des cuisiners", " un des chevaux du roi", " un traitre", " les récoles de blé", " une partie des écuries", " l'entièreté de la forêt", " plusieurs armes de différents soldats", " les clés de la prison", " durant un combat", " dans la forêt", " pour mieux se préparer à un combat", " les quartier royaux", " les équipement des soldats ce qui les gêne pour combattre", " des provisions", " certains soldats ennemis", " une partie de la citadelle", " les écuries", " ce qui nuit à la sécurité des travailleurs", " ce qui empêche le combat contre [villeAlea]", " les chevaux", " les combattants qui s'entrainent"]
    #Pour humains //// voler : De 0 à 1 : Negatif / 2 : neutre // tuer : De 3 à 4 : négatif / 5 : positif // bruler : De 6 à 8 : négatif // perdu : 9 : négatif / 10 neutre // endormi : 11 : negatif / 12 : neutre / 13 : positif // Pour annimaux : 14 à 17 // Pour météo : 18 à 23 // longueur : 23 

    $ i = 0
    while i != 5:
        $ villeAlea = listeVille[renpy.random.randint(0, 2)]
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
                    $ choix1 = "Mettre les chevaux en sécurité"
                    $ choix2 = "Préférer enfermer le coupable"
                elif(contextAlea == " l'entièreté de la forêt"):
                    $ choix1 = "Ce n'est pas grave"
                    $ choix2 = "Mieux vaut arrêter cette personne"
            
            elif(actionAlea == "a perdu"):
                $ contextAlea = listeContextuelle[renpy.random.randint(9, 10)]
                if(contextAlea == " plusieurs armes de différents soldats"):
                    $ choix1 = "Peu importe"
                    $ choix2 = "C'est très grave"
                elif(contextAlea == " les clés de la prison"):
                    $ choix1 = "Il métire une sanction humiliante"
                    $ choix2 = "Refaites-en d'autres"
            
            elif(actionAlea == "s'est endormi"):
                $ contextAlea = listeContextuelle[renpy.random.randint(11, 13)]
                if(contextAlea == " durant un combat"):
                    $ choix1 = "Comment est-ce possible"
                    $ choix2 = "Livrer-le directement à l'ennemi"
                elif(contextAlea == " dans la forêt"):
                    $ choix1 = "Que fait t'il dans la forêt"
                    $ choix2 = "Laisser-le"
                elif(contextAlea == " pour mieux se préparer à un combat"):
                    $ choix1 = "Pas de fainéants dans les rangs de l'armée"
                    $ choix2 = "Il a bien raison de se reposer"
            
            elif(actionAlea == "a donné(e) de quoi manger à une famille fauchée"):
                $ contextAlea = ""
                $ choix1 = "Que les pauvres restent pauvre"
                $ choix2 = "C'est une bonne action, cela pourra être utile plus tard"
            
            elif(actionAlea == "a aidé(e) un paysant à récolter le blé"):
                $ contextAlea = ""
                $ choix1 = "Il a bien fait de prendre de son temps pour aider"
                $ choix2 = "Il n'a pas le temps pour s'occuper de ça"
            
            elif(actionAlea == "a entraîné les soldats"):
                $ contextAlea = ""
                $ choix1 = "Féliciter"
                $ choix2 = "Dire qu'ils ne sont pas assez entrainés"
            
            elif(actionAlea == "a vaincu un village ennemi"):
                $ contextAlea = ""
                $ choix1 = "Faire une cérémonie pour célébrer cette victoire"
                $ choix2 = "Demmander de repartir au combat"
        elif(persoAlea == "Un chien" or persoAlea == "Un cochon" or persoAlea == "Un cheval"):
            #Annimaux
            $ actionAlea = listeAction[renpy.random.randint(9, 11)]
            if(actionAlea == "a sali"):
                $ contextAlea = listeContextuelle[renpy.random.randint(14, 15)]
                if(contextAlea == " les quartier royaux"):
                    $ choix1 = "C'est une insulte envers le roi"
                    $ choix2 = "Demander de nettoyer"
                elif(contextAlea == " les équipement des soldats ce qui les gêne pour combattre"):
                    $ choix1 = "Qu'ils continue à combattre"
                    $ choix2 = "Déclarer la défaite de la battaille"

            elif(actionAlea == "a dévoré"):
                $ contextAlea = listeContextuelle[renpy.random.randint(16, 17)]
                if(contextAlea == " des provisions"):
                    $ choix1 = "Ce ne sont que quelques résereves"
                    $ choix2 = "Allez en récolter d'autres"
                elif(contextAlea == " certains soldats ennemis"):
                    $ choix1 = "Féliciter cet annimal"
                    $ choix2 = "Les annimaux ne sont pas des combattants"
            
            elif(actionAlea == "a grandement aidé pendant une bataille contre [villeAlea]"):
                $ contextAlea = ""
                $ choix1 = "Envoyer plus d'annimaux aux combats"
                $ choix2 = "L'envoyer sur une autre bataille"

        elif(persoAlea == "Les innondations" or persoAlea == "Les intempéries" or persoAlea == "Le vent"):
            #Méteo
            $ actionAlea = listeAction[renpy.random.randint(12, 15)]
            if(actionAlea == "ont engloutis"):
                $ contextAlea = listeContextuelle[renpy.random.randint(18, 19)]
                if(contextAlea == " une partie de la citadelle"):
                    $ choix1 = "Evacuer les citoyens"
                    $ choix2 = "Ils peuvent bien se débrouiller tout seuls"
                elif(contextAlea == " les écuries"):
                    $ choix1 = "Les chevaux m'importe peu"
                    $ choix2 = "Evacuer les chevaux"
            
            elif(actionAlea == "rendent le sol glissant"):
                $ contextAlea = listeContextuelle[renpy.random.randint(20, 21)]
                if(contextAlea == " ce qui nuit à la sécurité des travailleurs"):
                    $ choix1 = "Mieux vaut assurer leur sécurité"
                    $ choix2 = "Pas question de faire une pause"
                elif(contextAlea == " ce qui empêche le combat contre [villeAlea]"):
                    $ choix1 = "Laissez-les combattre"
                    $ choix2 = "Battre en retraite"
            
            elif(actionAlea == "fait tomber des troncs d'abres sur"):
                $ contextAlea = listeContextuelle[renpy.random.randint(22, 23)]
                if(contextAlea == " les chevaux"):
                    $ choix1 = "Nous n'avons pas besoin de chevaux"
                    $ choix2 = "Mettez-les chevaux en sécurité"
                elif(contextAlea == " les combattants qui s'entrainent"):
                    $ choix1 = "Cessez leur entrainement"
                    $ choix2 = "Ce sera d'autant plus formateur"

            elif(actionAlea == "fait s'envoler [autrePersoAlea]"):
                $ contextAlea = ""
                $ choix1 = "Mettez tout le village à l'abri"
                $ choix2 = "Que chacun continue son activité"
        
        else:
            #En cas d'erreur
            $ i = 4
            o "humm, ce n'est pas censé arriver, nom du perso choisi aléatoirement : [persoAlea]"
            o "Réessayez s'il vous plaît"
            jump choix
        
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
                    $ messageSenateur = "Nous n'avons pas assez d'armes pour chaque soldats, mettez cette personne en prison."
                
                elif(choixDuJoueur == "Nous avons suffisament d'armes"):
                    $ messageSenateur = "Pas besoin de rechercher cette personne, nous avons largement assez d'armes pour tout le monde."
                
                elif(choixDuJoueur == "L'argent est bien trop important"):
                    $ messageSenateur = "Retrouvez-moi cet argent, nous en avons bien besoin pour pouvoir règner en maintre sur cet île."
                
                elif(choixDuJoueur == "Nous avons assez d'argent"):
                    $ messageSenateur = "Nous avons suffisament d'argent pour tenir jusqu'au prochaines conquêtes."
                
                elif(choixDuJoueur == "La nourriture est une denré précieuse"):
                    $ messageSenateur = "Nous avons besoin de toute nourriture, comdaner ce vol."
                
                elif(choixDuJoueur == "Ne me déranger pas pour un morceau de pain"):
                    $ messageSenateur = "Ce n'est qu'un bout de pain, restez sérieux."
            
            #Pour tuer
            elif(actionAlea == "a tué(e)"):
                if(choixDuJoueur == "Il y a d'autes cuistots"):
                    $ messageSenateur = "Tant pis, il y a bien d'autres cuisinier au royaume."
                
                elif(choixDuJoueur == "Arrêter le coupable"):
                    $ messageSenateur = "Arrêter cette personne !"

                elif(choixDuJoueur == "C'est un crime impardonable"):
                    $ messageSenateur = "Veuillez executer le coupable, voler le cheval du roi est un crime impardonable."
                
                elif(choixDuJoueur == "Il y a des dizaines de chevaux"):
                    $ messageSenateur = "Il y a des dizaines de chevaux dans les écuries, le roi peut bien en prendre un autre."
                
                elif(choixDuJoueur == "Il aurait mieux valu le juger"):
                    $ messageSenateur = "Il aurait été préférable de le juger avant de le tuer."
                
                elif(choixDuJoueur == "Féliciter"):
                    $ messageSenateur = "Bien, vous lui transmettrais mes félicitations."
            
            #Pour bruler
            elif(actionAlea == "a brulé"):
                if(choixDuJoueur == "L'enfermer"):
                    $ messageSenateur = "Mieux vaut l'enfermé avant que le pyromane ne recommence."
                
                elif(choixDuJoueur == "Ne rien faire"):
                    $ messageSenateur = "Nous n'avons pas les moyens de remplir nos prisons avec de tel énergumènes."
                
                elif(choixDuJoueur == "Mettre les chevaux en sécurité"):
                    $ messageSenateur = "La priorité est de mettre les chevaux en sécurité, on réfléchira à son cas plus tard."
                
                elif(choixDuJoueur == "Préférer enfermer le coupable"):
                    $ messageSenateur = "Mettez-moi cette personne au cachot, on s'occupera des chevaux plus tard."
                
                elif(choixDuJoueur == "Ce n'est pas grave"):
                    $ messageSenateur = "Elle ne nous appartient pas, ce n'est pas trop grave."
                
                elif(choixDuJoueur == "Mieux vaut arrêter cette personne"):
                    $ messageSenateur = "Il vaudrait mieux arrêter cette personne avant qu'elle s'attaque à notre village."

            #Pour perdu
            elif(actionAlea == "a perdu"):
                if(choixDuJoueur == "Peu importe"):
                    $ messageSenateur = "Nous en avons des milliers d'autres, dites à cette personne de ne par recommencer et de ne plus s'en occuper."

                elif(choixDuJoueur == "C'est très grave"):
                    $ messageSenateur = "Nous avons besoin de retrouver toutes ces armes le plus rapidement possible, en attendant mettez-le en prison."
                
                elif(choixDuJoueur == "Il métire une sanction humiliante"):
                    $ messageSenateur = "Mettez-le sur la place plublique et attendez que les citoyens lui balence des tomates à la figure."

                elif(choixDuJoueur == "Refaites-en d'autres"):
                    $ messageSenateur = "Ne me gêner pas pour si peu, refaites-en d'autres et n'en parlons plus."
            
            #Pour endormi
            elif(actionAlea == "s'est endormi"):
                if(choixDuJoueur == "Comment est-ce possible"):
                    $ messageSenateur = "Comment peut-on s'endormir en plein comabt ? Tuer cet individu."

                elif(choixDuJoueur == "Livrer-le à l'ennemi"):
                    $ messageSenateur = "Nous n'avons pas besoin d'unités de ce genre, laisser-le dormir sur le champs de bataille."
                
                elif(choixDuJoueur == "Que fait t'il dans la forêt"):
                    $ messageSenateur = "Comment ça dans la forêt ? Qu'il aille travailler."
                
                elif(choixDuJoueur == "Laisser-le"):
                    $ messageSenateur = "Laisser-le, il se ferra manger par la faune locale."
                
                elif(choixDuJoueur == "Pas de fainéants dans les rangs de l'armée"):
                    $ messageSenateur = "Il se reposera plus tard, pour l'instant qu'il aille au front."
                
                elif(choixDuJoueur == "Il a bien raison de se reposer"):
                    $ messageSenateur = "Il fait bien de se reposer, c'est mieux pour être performant au combat."
            
            #Pour famille fauchée
            elif(choixDuJoueur == "Que les pauvres restent pauvre"):
                $ messageSenateur = "Nous n'avons pas de temps à perdre avec les pauvres, qu'ilsrestent pauvre"
            
            elif(choixDuJoueur == "C'est une bonne action, cela pourra être utile plus tard"):
                $ messageSenateur = "C'est une bonne action qui pourra nous servir, cette famille pourra enter dans l'armée ou nous aider sur le plan politique"

            #Pour aider paysant à récolter
            elif(choixDuJoueur == "Il a bien fait de prendre de son temps pour aider"):
                $ messageSenateur = "C'est très bien, tout le monde devrait faire de même, le village serait beaucoup plus productif."
            
            elif(choixDuJoueur == "Il n'a pas le temps pour s'occuper de ça"):
                $ messageSenateur = "Il ferrait mieux de travailler sur ce qu'il sait faire, on a pas de temps a perdre, chacun à son poste !"
            
            #Entrainer soldats
            elif(choixDuJoueur == "Féliciter"):
                $ messageSenateur = "Tant mieux, les soldats seront plus performants, il mérite une récompense."

            elif(choixDuJoueur == "Dire qu'ils ne sont pas assez entrainés"):
                $ messageSenateur = "Qu'il continue à les entrainés, ils ont besoins d'être encore plus performants."
            
            #Vaincu un village rival
            elif(choixDuJoueur == "Faire une cérémonie pour célébrer cette victoire"):
                $ messageSenateur = "Prenons du temps pour nous reposer et être plus entrainés pour les prochaines batailles, c'est une victoire bien mérité."

            elif(choixDuJoueur == "Demmander de repartir au combat"):
                $ messageSenateur = "Pas de temps à perdre, que les soldats repartent au combat."
        
        elif(persoAlea == "Un chien" or persoAlea == "Un cochon" or persoAlea == "Un cheval"):
            #Pour annimaux
            #Pour salir
            if(actionAlea == "a sali"):
                if(choixDuJoueur == "C'est une insulte envers le roi"):
                    $ messageSenateur = "Exectuer cet annimal, c'est une insulte envers le roi"
                
                elif(choixDuJoueur == "Demander de nettoyer"):
                    $ messageSenateur = "Commencez par nettoyer, je demanderai l'avis du roi sur ce qu'on fait de cet annimal"
                
                elif(choixDuJoueur == "Qu'ils continue à combattre"):
                    $ messageSenateur = "Que les soldats continue de combattre, leur prochain combat leur paraitra plus simple."
                
                elif(choixDuJoueur == "Déclarer la défaite de la battaille"):
                    $ messageSenateur = "Il me semble plus important de déclarer une défaite que de perdre des hommes inutilement."
            
            #Pour dévorer
            elif(actionAlea == "a dévoré"):
                if(choixDuJoueur == "Ce ne sont que quelques résereves"):
                    $ messageSenateur = "Ce n'est pas très grâve il nous reste de bons stocks de provision, ce n'était que quelques réserves."
                
                elif(choixDuJoueur == "Allez en récolter d'autres"):
                    $ messageSenateur = "Condamnez-moi cet annimal et trouvez-en d'autres."
                
                elif(choixDuJoueur == "Féliciter cet annimal"):
                    $ messageSenateur = "Félicitez moi cet annimal."

                elif(choixDuJoueur == "Les annimaux ne sont pas des combattants"):
                    $ messageSenateur = "Peu importe les annimaux ne sont pas des combattants."
            
            #Pour aider pendant un combat
            elif(choixDuJoueur == "Envoyer plus d'annimaux sur les prochain combat"):
                $ messageSenateur = "C'est une bonne stratégie pour les prochains comabts, nous enverrons plus d'annimaux la prochaine fois."
            
            elif(choixDuJoueur == "L'envoyer sur une autre bataille"):
                $ messageSenateur = "Parfait, envoyez-le sur un autre champ de bataille pour qu'il puise faire de même."
        
        elif(persoAlea == "Les innondations" or persoAlea == "Les intempéries" or persoAlea == "Le vent"):
            #Pour météo
            #Pour engloutis
            if(actionAlea == "ont engloutis"):
                if (choixDuJoueur == "Evacuer les citoyens"):
                    $ messageSenateur = "Prenons du temps pour évacuer les citoyens."

                elif(choixDuJoueur == "Ils peuvent bien se débrouiller tout seuls"):
                    $ messageSenateur = "Nous avons d'autres problèmes à gérer, ils peuvent bien règler ce problème d'innondations seuls."

                elif(choixDuJoueur == "Les chevaux m'importe peu"):
                    $ messageSenateur = "Les chevaux ont peu d'importance pour gagner les batailles."
                
                elif(choixDuJoueur == "Evacuer les chevaux"):
                    $ messageSenateur = "Mettez les chevaux dans un endroi plus sûr."
            
            #Pour sol glissant
            elif(actionAlea == "rendent le sol glissant"):
                if (choixDuJoueur == "Mieux vaut assurer leur sécurité"):
                    $ messageSenateur = "La sécurité des travailleurs est primordiale si l'on veut conquérir l'entièreté de cette île."

                elif(choixDuJoueur == "Pas question de faire une pause"):
                    $ messageSenateur = "Pas questions que les travailleurs fassent des heures en moins."
                
                elif(choixDuJoueur == "Laissez-les combattre"):
                    $ messageSenateur = "Le temps peut être en notre avantage si il gêne les adversaires, laissez-les combattre."

                elif(choixDuJoueur == "Battre en retraite"):
                    $ messageSenateur = "Il serait préférable de battre en retraite pour éviter de perdre des hommes."
            
            #Pour troncs d'arbres
            elif(actionAlea == "fait tomber des troncs d'abres sur"):
                if (choixDuJoueur == "Nous n'avons pas besoin de chevaux"):
                    $ messageSenateur = "Tant pis pour les chevaux, nous n'en avons pas vraiment besoin de toute façon."
                
                elif(choixDuJoueur == "Mettez-les chevaux en sécurité"):
                    $ messageSenateur = "Les chevaux sont trop précieaux pour les batailles, mettez-les en sécurité."

                elif(choixDuJoueur == "Cessez leur entrainement"):
                    $ messageSenateur = "Mieux vaut les mettre en sécurité, cessez leur entrainement."
                
                elif(choixDuJoueur == "Ce sera d'autant plus formateur"):
                    $ messageSenateur = "Ils seront mieux formés après, qu'ils continuent leur entrainement."
            
            #Envol de [persoAlea]
            elif(choixDuJoueur == "Mettez tout le village à l'abri"):
                $ messageSenateur = "Mieux vaut mettre tout le monde à l'abir le temps que la tempête se calme."

            elif(choixDuJoueur == "Que chacun continue son activité"):
                $ messageSenateur = "Que tout le monde reste à son poste, nous n'avons pas temps à perdre, je ne tolérerai pas une defaite."
        else:
            #En cas d'erreur
            $ messageSenateur = "Humm, c'est une erreur... Réessayez s'il vous plaît"
        s "[messageSenateur]"
    jump choix