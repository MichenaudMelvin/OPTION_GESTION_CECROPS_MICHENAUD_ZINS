label strategieMap:
    call screen conquete_map

label islesbury:
    $ villageChoisi = "Islesbury"
    jump conquete

label redwater:
    $ villageChoisi = "Redwater"
    jump conquete

label swanford:
    $ villageChoisi = "Swanford"
    jump conquete

label ourBase:
    o "Heu... monsieur le sénateur... c'est notre base..."
    jump strategieMap

label conquete:
    $ possibiliteFarm = True
    s "Bien, attaquons [villageChoisi] !"
    o "Pour rappel [villageChoisi] : est composé de x hommes"
    #il faudrait mieux faires des classes pour chaque ville
    if(king == 1 and villageChoisi == "Islesbury" and debutJeu == True):
        o "Woah, vous voulez déjà vous attaquer à [villageChoisi] ?! Je vous rappele que c'est la plus grande puissance de l'île !"
    elif(king == 2 and villageChoisi == "Redwater" and debutJeu == True):
        o "Woah, vous voulez déjà vous attaquer à [villageChoisi] ?! Je vous rappele que c'est la plus grande puissance de l'île !"
    elif(king == 2 and villageChoisi == "Swanford" and debutJeu == True):
        o "Woah, vous voulez déjà vous attaquer à [villageChoisi] ?! Je vous rappele que c'est la plus grande puissance de l'île !"
    
    menu:
        o "Voulez-vous toujours attaquer [villageChoisi] ?"
        "Oui":
            s "Oui, allons-y !"
        "Non":
            jump jeu
    
    s "et paf"