from voiture import Voiture
from crud_db import ajouter_voiture, supprimer_voiture, recuperer_voitures


# 1. AJOUT DE VOITURE

v1 = Voiture("Mercedes", "Classe C", 2024, 55000)
ajouter_voiture(v1)

print("Ajout de la Mercedes terminé")
print("----------------------")


# 2. SUPPRESSION DE VOITURE

# IMPORTANT : vérifier l'ID dans MySQL
supprimer_voiture(1)

print("Suppression de la Mercedes terminée")
print("----------------------")


# 3. RECUPERATION + AFFICHAGE

voitures = recuperer_voitures()

print("Liste des voitures dans la base :")

for v in voitures:
    v.afficher_voiture()

print("----------------------")