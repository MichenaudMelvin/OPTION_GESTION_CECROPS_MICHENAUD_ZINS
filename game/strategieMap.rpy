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
        humainEnvoyes = renpy.input("Bien, entrez le nombre d'hommes que vous voulez envoyer au combat : ", length=3)
        #besoin des expressions régulières / rationnelles pour éviter une erreur. see : https://www.w3schools.com/jsref/jsref_regexp_not_0-9.asp
        #https://www.youtube.com/watch?v=ev0oVuN_hkA
        #https://www.kite.com/python/answers/how-to-convert-a-list-of-integers-into-a-single-integer-in-python#
        if not humainEnvoyes:
            humainEnvoyes = 0
        #not working
        # import re
        # conversion = re.findall("([0-9]+)", humainEnvoyes)
        # conversionStr = [str(integer) for interger in conversion]
        # a_string = "".join(conversionStr)
        # resultat = int(a_string)

    $ joueur.humainEpuises(resultat)
    if(joueur.getHumainEpuises > joueur.getRessourceHumain):
        o "Vous n'avez pas assez d'Hommes pour combatre, veuillez réduire vos ambitions. [joueur.getHumainEpuises], [joueur.getRessourceHumain]"
        $ joueur.humainEpuises(-resultat)
        jump combat
    elif(joueur.getHumainEpuises == 0):
        o "Humm... vous n'avez envoyé personne..."
        jump combat
    s "[conversionStr]"

    $ villageChoisi.defeatVillage(True)
    if(villageChoisi.getDefeatVillage() == True and villageChoisi.getKing() == True):
        jump victory
    elif(villageChoisi.getDefeatVillage() == True):
        o "Nous avons récupérés [villageChoisi.getRessourceBois] ressources de bois et [villageChoisi.getRessourcePierre] ressources de pierre de [villageChoisi.getNomVillage]."
        o "Et [villageChoisi.getRessourceHumain] hommes ont rejoint nos rangs."
        $ joueur.addRessources(villageChoisi.getRessourceBois, villageChoisi.getRessourcePierre, villageChoisi.getRessourceHumain)
        $ villageChoisi.addRessources(-villageChoisi.getRessourceBois, -villageChoisi.getRessourcePierre, -villageChoisi.getRessourceHumain)
    else:
        $ perteBois = (joueur.getRessourceBois)/2
        $ pertePierre = (joueur.getRessourcePierre)/2
        $ perteHumain = (joueur.getRessourceHumain)/4
        o "Nous avons perdu [perteBois] ressources de bois et [pertePierre] ressources de pierre."
        o "Et [perteHumain] hommes ont quittés nos rangs."
        $ joueur.addRessources(-perteBois, -pertePierre, -perteHumain)
        $ villageChoisi.addRessources(perteBois, pertePierre, perteHumain)
    
    show text "[joueur.getRessourceBois]\n\n\n\n\n[joueur.getRessourcePierre]\n\n\n\n\n[joueur.getRessourceHumain]\n\n\n\n[joueur.getHumainEpuises]":
        xalign 0.14
        yalign 0.1
    
    $ joueur.possibiliteFarm(True)
    $ joueur.avanceJeu()
    jump choix

