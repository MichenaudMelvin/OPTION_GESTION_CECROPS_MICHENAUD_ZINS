label strategieMap:
    call screen conquete_map

label islesbury:
    $ islesbury.choixVillage(True)
    jump conquete

label redwater:
    $ redwater.choixVillage(True)
    jump conquete

label swanford:
    $ swanford.choixVillage(True)
    jump conquete

label ourBase:
    o "Heu... monsieur le sénateur... c'est notre base..."
    jump strategieMap

label conquete:
    $ joueur.possibiliteFarm(True)
    s "Bien, attaquons [villageChoisi] !"
    o "Pour rappel [villageChoisi] : est composé de x hommes"
    #il faudrait mieux faires des classes pour chaque ville
    if(islesbury.getKing == True and islesbury.getVillageChoisi == True and joueur.getDebutJeu == True):
        o "Woah, vous voulez déjà vous attaquer à [villageChoisi] ?! Je vous rappele que c'est la plus grande puissance de l'île !"
    elif(redwater.getKing == True and redwater.getVillageChoisi == True and joueur.getDebutJeu == True):
        o "Woah, vous voulez déjà vous attaquer à [villageChoisi] ?! Je vous rappele que c'est la plus grande puissance de l'île !"
    elif(swanford.getKing == True and swanford.getVillageChoisi == True and joueur.getDebutJeu == True):
        o "Woah, vous voulez déjà vous attaquer à [villageChoisi] ?! Je vous rappele que c'est la plus grande puissance de l'île !"
    
    menu:
        o "Voulez-vous toujours attaquer [villageChoisi] ?"
        "Oui":
            s "Oui, allons-y !"
        "Non":
            jump jeu
    
    s "et paf"