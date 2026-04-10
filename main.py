from voiture import Voiture
from crud_db import modifier_voiture

v1 = Voiture("Audi", "A3", 2026, 62000, 1)

modifier_voiture(v1)

print("Voiture modifiée avec succès")