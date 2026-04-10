from crud_db import recuperer_voitures

voitures = recuperer_voitures()

for v in voitures:
    v.afficher_voiture()