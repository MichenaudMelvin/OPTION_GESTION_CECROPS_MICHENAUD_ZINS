label strategieMap:
    call screen conquete_map

label islesbury:
    s "Ok"

    s "J'ai la dalle, on attaque Islebury"

    jump finish

label redwater:

    s "Ok"

    s "J'ai la dalle, on attaque Redwater"

    jump finish

label swanford:
    s "Ok"

    s "J'ai la dalle, on attaque Swanford"

    jump finish

label ourBase:

    o "Heu... monsieur le sénateur... c'est notre base..."
    jump strategieMap

label finish:

    s "voila, c'est a peu près à ça que ça va ressembler"
    s "le nom des villes est a revoir je pense mais c'est deja pas mal"
    return