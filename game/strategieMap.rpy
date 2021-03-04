label strategieMap:
    call screen conquete_map

label islesbury:
    $ villageChoisi = islesbury
    jump conquete

label redwater:
    $ villageChoisi = redwater
    jump conquete

label swanford:
    $ villageChoisi = swanford
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
            $ joueur.possibiliteFarm(True)
            $ joueur.avanceJeu()
        "Non":
            jump jeu
    
    s "et paf"
    jump strategieMap