#
# Batiment caserne
#

label menuCaserne:
    menu:
        "Entraîner des troupes":
            jump creerUnite
        "Améliorer le bâtiment":
            $ batimentChoisi = caserne
            jump upgrade_building
        "Attaquer des villages ennemis":
            jump strategieMap
        "Ne rien faire":
            jump choix

label creerUnite:
    $ fighters_nbr = renpy.input("Combien voulez-vous en entraîner ?", allow="0123456789", length=3)
    python:
        fighters_nbr = int(fighters_nbr)
    $ coutBois = fighters_nbr*2
    $ coutPierre = fighters_nbr*3
    if(coutBois > joueur.getRessourceBois):
        o "Vous n'avez pas assez de bois pour former ces unités"
        jump creerUnite
    if(coutPierre > joueur.getRessourcePierre):
        o "Vous n'avez pas assez de pierre pour former ces unités"
        jump creerUnite
    if fighters_nbr == 0:
        o "Vous n'avez pas formé de guerrier."
    elif fighters_nbr == 1:
        o "Vous avez formé [fighters_nbr] guerrier."
        o "Cela vous a couté [coutBois] bois et [coutPierre] pierres"
    elif fighters_nbr > 1:
        o "Vous avez formé [fighters_nbr] guerriers."
        o "Cela vous a couté [coutBois] bois et [coutPierre] pierres"
    
    $ joueur.addRessources(-coutBois, -coutPierre, (fighters_nbr+joueur.getHumainEpuises))
    $ joueur.humainEpuises(-joueur.getHumainEpuises)
    $ joueur.possibiliteFarm(True)
    o "Vous possédez maintenant [joueur.getRessourceHumain] unités."
    jump choix

#
# Batiment Mine
#

label menuMine:
    menu:
        "Récupérer des ressources":
            jump framRessources
        "Améliorer le batiment":
            $ batimentChoisi = mine
            jump upgrade_building
        "Ne rien faire":
            jump choix

#
# Batiment Senat
#

label menuSenat: 
    menu:
        "Appeler votre assisant":
            jump diplomatie
        "Améliorer":
            $ batimentChoisi = senat
            jump upgrade_building
        "Ne rien faire":
            jump choix

#besoin que les niveau des batiments servent à quelquechose
label upgrade_building:
    menu:
        o "Êtes-vous sûr de vouloir aggrandir votre [batimentChoisi.getType] ?"
        "Aggrandir":
            #besoin d'améliorer le sénat pour pouvoir améliorer les autres batiments
            if(batimentChoisi == senat and senat.getNiveau < 3):
                $ coutRessources = -100 * batimentChoisi.getNiveau
                if(coutRessources > joueur.getRessourceBois or coutRessources > joueur.getRessourcePierre):
                    o "Vous n'avez pas assez de ressources pour améliorer votre [batimentChoisi]"
                    jump choix
                $ batimentChoisi.niveauSup()
                $ joueur.addRessources(coutRessources, coutRessources, 0)
                o "Votre [batimentChoisi.getType] est maintenant niveau [batimentChoisi.getNiveau]."
            elif(batimentChoisi.getNiveau < 3 and batimentChoisi.getNiveau < senat.getNiveau):
                $ coutRessources = -50 * batimentChoisi.getNiveau
                if(coutRessources > joueur.getRessourceBois or coutRessources > joueur.getRessourcePierre):
                    o "Vous n'avez pas assez de ressources pour améliorer votre [batimentChoisi]"
                    jump choix
                $ batimentChoisi.niveauSup()
                $ joueur.addRessources(coutRessources, coutRessources, 0)
                o "Votre [batimentChoisi.getType] est maintenant niveau [batimentChoisi.getNiveau]."
            elif(batimentChoisi.getNiveau == 3):
                o "Votre [batimentChoisi.getType] est déjà au niveau maximum."
            elif(batimentChoisi.getNiveau >= senat.getNiveau):
                o "Vous devez d'abord améliorer votre sénat"
            if(caserne.getNiveau == 3 and mine.getNiveau == 3 and senat.getNiveau == 3):
                jump defaite
            else:
                jump choix
        "Ne rien faire":
            jump choix

#save du programme de kilian // à voir si on garde le système de différents type de combatants ou pas.
# "Archer":
#     jump nbr_archer
# "Cavalier":
#     jump nbr_cavalier
# label nbr_archer:
#     $ fighters_nbr = renpy.input("Combien voulez-vous en entraîner ?", allow="0123456789", length=2)
#     python:
#         fighters_nbr = int(fighters_nbr)
#     $ nombre_archer = fighters_nbr + nombre_archer
#     if fighters_nbr == "0":
#         o "Vous n'avez pas formé d'archer."
#     if fighters_nbr == "1":
#         o "Vous avez formé [fighters_nbr] archer."
#     if fighters_nbr > "1":
#         o "Vous avez formé [fighters_nbr] archers."
#     jump batiments

# label nbr_cavalier:
#     $ fighters_nbr = renpy.input("Combien voulez-vous en entraîner ?", allow="0123456789", length=2)
#     python:
#         fighters_nbr = int(fighters_nbr)
#     $ nombre_cavalier = fighters_nbr + nombre_cavalier
#     if fighters_nbr == "0":
#         o "Vous n'avez pas formé de cavalier."
#     if fighters_nbr == "1":
#         o"Vous avez formé [fighters_nbr] cavalier."
#     if fighters_nbr > "1":
#         o "Vous avez formé [fighters_nbr] cavaliers."
#     jump batiments