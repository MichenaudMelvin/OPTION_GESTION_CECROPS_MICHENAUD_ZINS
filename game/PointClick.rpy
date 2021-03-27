screen senat:
    imagebutton:
        xpos 500
        ypos 360
        idle "senat.png"
        hover "senathover.png"
        at senat_zoom
        action [Hide("arbre"), Hide("arene"), Hide("senat"), Jump("menuSenat")]

screen arbre:
    imagebutton:
        xpos 350
        ypos 400
        idle "arbre.png"
        hover "arbrehover.png"
        at arbre_zoom
        action [Hide("senat"), Hide("arene"), Hide("arbre"), Jump("menuMine")]

screen arene:
    imagebutton:
        xpos 800
        ypos 360
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

screen senatTuto:
    imagebutton:
        xpos 500
        ypos 360
        idle "senat.png"
        at senat_zoom

screen arbreTuto:
    imagebutton:
        xpos 350
        ypos 400
        idle "arbre.png"
        at arbre_zoom

screen areneTuto:
    imagebutton:
        xpos 800
        ypos 360
        idle "arena.png"
        at arena_zoom

screen senatTutoHover:
    imagebutton:
        xpos 500
        ypos 360
        idle "senathover.png"
        at senat_zoom

screen arbreTutoHover:
    imagebutton:
        xpos 350
        ypos 400
        idle "arbrehover.png"
        at arbre_zoom

screen areneTutoHover:
    imagebutton:
        xpos 800
        ypos 360
        idle "arenahover.png"
        at arena_zoom