label strategieMap:
    call screen conquete_map

label islesbury:
    if(king == 1):
        menu:
            o "Woah, vous voulez deja vous attaquez à la plus grande puissance de l'île ??"
            "Oui":
                $ possibiliteFarm = True
                jump finish
            "Non":
                jump finish
    else:
        s "Ok"

        s "J'ai la dalle, on attaque Islebury"
        $ possibiliteFarm = False
        jump finish

label redwater:
    if(king == 2):
        menu:
            o "Woah, vous voulez deja vous attaquez à la plus grande puissance de l'île ??"
            "Oui":
                $ possibiliteFarm = True
                jump finish
            "Non":
                jump finish
    else:
        s "Ok"

        s "J'ai la dalle, on attaque Redwater"
        $ possibiliteFarm = False
        jump finish

label swanford:
    if(king == 3):
        menu:
            o "Woah, vous voulez deja vous attaquez à la plus grande puissance de l'île ??"
            "Oui":
                $ possibiliteFarm = True
                jump finish
            "Non":
                jump finish
    else:
        s "Ok"

        s "J'ai la dalle, on attaque Swanford"
        $ possibiliteFarm = False
        jump finish

label ourBase:

    o "Heu... monsieur le sénateur... c'est notre base..."
    jump strategieMap

label finish:

    s "voila, c'est a peu près à ça que ça va ressembler"
    s "le nom des villes est a revoir je pense mais c'est deja pas mal"
    return