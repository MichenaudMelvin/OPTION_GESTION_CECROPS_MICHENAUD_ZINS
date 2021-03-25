screen senat:
    imagebutton:
        xpos 600
        ypos 360
        idle "senat.png"
        hover "senathover.png"
        at senat_zoom
        action [Hide("arbre"), Hide("arene"), Hide("senat"), Jump("menuSenat")]

screen arbre:
    imagebutton:
        xpos 250
        ypos 450
        idle "arbre.png"
        hover "arbrehover.png"
        at arbre_zoom
        action [Hide("senat"), Hide("arene"), Hide("arbre"), Jump("menuMine")]

screen arene:
    imagebutton:
        xpos 800
        ypos 220
        idle "arena.png"
        hover "arenahover.png"
        at arena_zoom
        action [Hide("senat"), Hide("arbre"), Hide("arene"), Jump("menuCaserne")]

transform senat_zoom:        
    zoom 0.5
transform arbre_zoom:
    zoom 0.2
transform arena_zoom:
    zoom 0.3