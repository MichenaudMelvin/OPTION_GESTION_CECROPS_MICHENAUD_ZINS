# init python:
#     choixSenat = []
#     #Menu qui permet de choisir les différentes actions possibles du jeu // repris du tuto renpy
#     class TitreSenat(object):
#         def __init__(self, title):
#             self.kind = "titre"
#             self.title = title

#             choixSenat.append(self)

#     class MenuSenat(object):
#         def __init__(self, label, title, move=True):
#             self.kind = "choix"
#             self.label = label
#             self.title = title

#             if move and (move != "after"):
#                 self.move_before = True
#             else:
#                 self.move_before = False

#             if move and (move != "before"):
#                 self.move_after = True
#             else:
#                 self.move_after = False

#             choixSenat.append(self)

#     TitreSenat(_("Que faire ?"))
#     MenuSenat("ameliorerSenat", _("Améliorer"))
#     MenuSenat("diplomatie", _("Appeler l'assistant"))

# screen menuSenat(adj):
#     frame:
#         xsize 640
#         xalign .5
#         ysize 485
#         ypos 30
#         has side "c r b"
#         viewport:
#             yadjustment adj
#             mousewheel False
#             vbox:
#                 for i in choixSenat:
#                     if i.kind == "choix":
#                         textbutton i.title:
#                             action Return(i)
#                             left_padding 20
#                             xfill True
#                     else:
#                         null height 10
#                         text i.title alt ""
#                         null height 5
#         bar adjustment adj style "vscrollbar"
#         textbutton _("Faire autre chose"):
#             xfill True
#             action Return(False)
#             top_margin 10

# label menuSenat:
#     $ renpy.choice_for_skipping()
#     call screen menuSenat(adj=menu_adjustment)
#     $ tutorial = _return
#     if not tutorial:
#         jump end
    
#     call expression tutorial.label
#     jump choix