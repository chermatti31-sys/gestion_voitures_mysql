from voiture import Voiture
from crud_db import ajouter_voiture, supprimer_voiture, recuperer_voitures


v1 = Voiture("Mercedes", "Classe C", 2024, 55000)

ajouter_voiture(v1)

print("Mercedes ajoutée avec succès")