from voiture import Voiture
from crud_db import ajouter_voiture, supprimer_voiture, recuperer_voitures


voitures = recuperer_voitures()

print("Liste des voitures dans la base :")

for v in voitures:
    v.afficher_voiture()