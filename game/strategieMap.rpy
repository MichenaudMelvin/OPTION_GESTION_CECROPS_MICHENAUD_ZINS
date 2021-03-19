label strategieMap:
    call screen conquete_map

label islesbury:
    $ villageChoisi = islesbury
    if(villageChoisi.getDefeatVillage() == True):
        o "Heum, nous avons déjà détruit ce village"
        jump strategieMap
    else:
        jump conquete

label redwater:
    $ villageChoisi = redwater
    if(villageChoisi.getDefeatVillage() == True):
        o "Heum, nous avons déjà détruit ce village"
        jump strategieMap
    else:
        jump conquete

label swanford:
    $ villageChoisi = swanford
    if(villageChoisi.getDefeatVillage() == True):
        o "Heum, nous avons déjà détruit ce village"
        jump strategieMap
    else:
        jump conquete

label ourBase:
    o "Heu... monsieur le sénateur... c'est notre base..."
    jump strategieMap

label conquete:
    s "Bien, attaquons [villageChoisi.getNomVillage] !"
    if(villageChoisi.getKing() == True and joueur.getDebutJeu() == True):
        o "Woah, vous voulez déjà vous attaquer à [villageChoisi.getNomVillage] ?! Je vous rappele que c'est la plus grande puissance de l'île !"
    
    o "Pour rappel [villageChoisi.getNomVillage] : est composé de [villageChoisi.getRessourceHumain] hommes"
    
    menu:
        o "Voulez-vous toujours attaquer [villageChoisi.getNomVillage] ?"
        "Oui":
            s "Oui, allons-y !"
            jump combat
        "Non":
            jump choix

label combat:
    python:
        humainEnvoyes = renpy.input("Bien, entrez le nombre d'hommes que vous voulez envoyer au combat : ", allow="0123456789", length=3)
        if not humainEnvoyes:
            humainEnvoyes = 0
        intHumainEnvoyes = int(humainEnvoyes)

    if(intHumainEnvoyes > joueur.getRessourceHumain):
         menu:
            o "Vous n'avez pas assez d'Hommes pour combatre, veuillez réduire vos ambitions."
            "faire autre chose":
                jump choix
            "recommencer":
                jump combat
    elif(intHumainEnvoyes == 0):
        menu:
            o "Humm... vous n'avez envoyé personne..."
            "faire autre chose":
                jump choix
            "recommencer":
                jump combat    
    $ humainEnvoyesParVillageChoisi = villageChoisi.humainEnvoyesParVillegaeEnnemi()
    
    python:
        #ajouter la jauge d'affection à coder dans #diplomatie.rpy
        #possiblement à revoir
        #reduction des humains par un chiffre aléatoire entre 0 et 1, float // la réduction correspond au nombre d'humains mort au combat
        #+/- de perte en fonction de la diplomatie du joueur.
        resultatCombatJoueur = int(intHumainEnvoyes * (renpy.random.uniform(0, 1) + joueur.getNiveauDiplomatie))
        if(resultatCombatJoueur > intHumainEnvoyes):
            resultatCombatJoueur = intHumainEnvoyes
        elif(resultatCombatJoueur < 0):
            resultatCombatJoueur = 0
        humainJoueurMorts = intHumainEnvoyes - resultatCombatJoueur
        
        #reduction des humains par un chiffre aléatoire entre 0.5 et 1, float // la réduction correspond au nombre d'humains mort au combat
        resultatCombatEnnemi = int(humainEnvoyesParVillageChoisi * renpy.random.uniform(0.5, 1))
        humainEnnemiMorts = humainEnvoyesParVillageChoisi - resultatCombatEnnemi
    
    s "[joueur.getNiveauDiplomatie]"
    pause 2
    s "Sur nos [intHumainEnvoyes] humains envoyés, il reste [resultatCombatJoueur] hommes, les [humainJoueurMorts] autres sont morts."
    s "Sur les [humainEnvoyesParVillageChoisi] humains envoyés par [villageChoisi.getNomVillage], ils leurs en restent [resultatCombatEnnemi] et [humainEnnemiMorts] de leurs hommes sont morts."
    if(resultatCombatJoueur > resultatCombatEnnemi):
        $ villageChoisi.defeatVillage(True)
    elif(resultatCombatJoueur <= resultatCombatEnnemi):
        $ villageChoisi.defeatVillage(False)
    else:
        s "Normalement cette situation n'est pas possible."
        jump choix
    
    $ joueur.addRessources(0, 0, joueur.getHumainEpuises)
    $ joueur.humainEpuises(-joueur.getHumainEpuises)
    if(villageChoisi.getDefeatVillage() == True and villageChoisi.getKing() == True):
        #si le joueur gagne contre le village maitre de l'ile : condition de victoire du jeu.
        jump victory
    elif(villageChoisi.getDefeatVillage() == True):
        #si le joueur gagne contre l'ennemi, gain de toutes les ressources du village adverse
        o "Nous avons récupérés [villageChoisi.getRessourceBois] ressources de bois et [villageChoisi.getRessourcePierre] ressources de pierre de [villageChoisi.getNomVillage]."
        o "Et [villageChoisi.getRessourceHumain] hommes ont rejoint nos rangs, [resultatCombatJoueur] hommes ont besoin de se reposer."
        $ joueur.addRessources(villageChoisi.getRessourceBois, villageChoisi.getRessourcePierre, villageChoisi.getRessourceHumain)
        $ villageChoisi.addRessources(-villageChoisi.getRessourceBois, -villageChoisi.getRessourcePierre, -villageChoisi.getRessourceHumain)
        $ joueur.humainEpuises(resultatCombatJoueur)
    else:
        #si le joueur perd contre l'ennemi, perte de la moitié de ses ressources qui sont envoyés au village adverse.
        $ perteBois = (joueur.getRessourceBois)/2
        $ pertePierre = (joueur.getRessourcePierre)/2
        #perte de la moitié des humains restants
        $ perteHumain = resultatCombatJoueur/2
        $ restePerteHumain = resultatCombatJoueur%2
        $ joueur.humainEpuises(perteHumain+restePerteHumain)
        $ joueur.addRessources(-perteBois, -pertePierre, -resultatCombatJoueur-humainJoueurMorts)
        $ villageChoisi.addRessources(perteBois, pertePierre, perteHumain)
        o "Nous avons perdu [perteBois] ressources de bois et [pertePierre] ressources de pierre."
        o "Et [perteHumain] hommes ont quittés nos rangs, [joueur.getHumainEpuises] hommes ont besoin de se reposer."
    
    $ joueur.possibiliteFarm(True)
    $ joueur.avanceJeu()
    jump choix