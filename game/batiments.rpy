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
    
    if fighters_nbr == 0:
        o "Vous n'avez pas formé de guerrier."
    elif fighters_nbr == 1:
        o "Vous avez formé [fighters_nbr] guerrier."
        o "cela vous a couté X trucs"
    elif fighters_nbr > 1:
        o "Vous avez formé [fighters_nbr] guerriers."
        o "cela vous a couté X trucs"
    
    $ joueur.addRessources(-5, -8, fighters_nbr)
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

label ameliorerMine:
    if mine.getNiveau < 3:
        $ mine.niveauSup()
        $ cout = -10 * mine.getNiveau
        $ joueur.addRessources(cout, cout)
        o "Votre mine est maintenant niveau [mine.getNiveau]."
    else:
        o "Vous ne pouvez plus améliorer votre mine."
    jump choix

#
# Batiment Senat
#

label menuSenat: 
    menu:
        "Améliorer":
            $ batimentChoisi = senat
            jump upgrade_building
        "Apelez votre assisant":
            jump diplomatie
        "Ne rien faire":
            jump choix

#besoin que les niveau des batiments servent à quelquechose
label upgrade_building:
    menu:
        o "Êtes-vous sûr de vouloir aggrandir votre [batimentChoisi.getType] ?"
        "Aggrandir":
            if batimentChoisi.getNiveau < 3:
                $ batimentChoisi.niveauSup()
                $ coutRessources = -10 * batimentChoisi.getNiveau
                $ joueur.addRessources(coutRessources, coutRessources, 0)
                o "Votre [batimentChoisi.getType] est maintenant niveau [batimentChoisi.getNiveau]."
            else:
                o "Vous [batimentChoisi.getType] est déjà au niveau maximum."
            jump choix
        "Ne rien faire":
            jump choix

#save du programme de killian // à voir si on garde le système de différents type de combatants ou pas.
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