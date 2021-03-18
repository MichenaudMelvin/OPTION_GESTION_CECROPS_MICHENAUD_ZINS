screen senat:
    imagebutton:
        xpos 600
        ypos 360
        idle "senat.png"
        at custom_senat
        action [Hide("senat"), Hide("arbre"), Hide("arene"), Jump("interieur_senat")]

screen arbre:
    imagebutton:
        xpos 190
        ypos 450
        idle "arbre.png"
        at custom_arbre
        action [Hide("senat"), Hide("arbre"), Hide("arene"), Jump("arbre")]

screen leave:
    imagebutton:
        xpos 1100
        ypos 550
        idle "leave.png"
        at return_zoom
        action [Jump("start")]

screen arene:
    imagebutton:
        xpos 800
        ypos 220
        idle "arena2.png"
        at custom_arena
        action [Hide("senat"), Hide("arbre"), Hide("arene"), Jump("interieur_arene")]
    


transform custom_senat:        
    zoom 0.5
transform custom_arbre:
    zoom 0.2
transform return_zoom:
    zoom 0.3
transform custom_arena:
    zoom 0.3