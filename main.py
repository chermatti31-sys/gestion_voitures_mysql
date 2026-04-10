from voiture import Voiture
from crud_db import ajouter_voiture, supprimer_voiture, recuperer_voitures, modifier_voiture


# 1. AJOUT DES VOITURES

v1 = Voiture("Audi", "A3", 2025, 60000)
v2 = Voiture("BMW", "M3", 2026, 65000)

ajouter_voiture(v1)
ajouter_voiture(v2)

print("Ajout des voitures terminé")
print("----------------------")


# 2. SUPPRESSION D'UNE VOITURE

supprimer_voiture(2)

print("Suppression de la voiture id 2 terminée")
print("----------------------")


# 3. RECUPERATION + AFFICHAGE

liste_voitures = recuperer_voitures()

print("Liste des voitures dans la base :")
for voiture in liste_voitures:
    voiture.afficher_voiture()

print("----------------------")


# 4. MODIFICATION D'UNE VOITURE

v_modifiee = Voiture("Audi", "A3 Sport", 2026, 62000, 1)
modifier_voiture(v_modifiee)

print("Modification de la voiture id 1 terminée")
print("----------------------")


# 5. AFFICHAGE FINAL

liste_voitures = recuperer_voitures()

print("Après modification :")
for voiture in liste_voitures:
    voiture.afficher_voiture()



from voiture import Voiture
from crud_db import ajouter_voiture, supprimer_voiture, recuperer_voitures

#AJOUTER UNE VOITURE MERCEDES PUI LA SUPPRIMER PUIS LA RÉCUPERER,

# 1. AJOUT DE VOITURE

v1 = Voiture("Mercedes", "Classe C", 2024, 55000)
ajouter_voiture(v1)

print("Ajout de la Mercedes terminé")
print("----------------------")


# 2. SUPPRESSION DE VOITURE

supprimer_voiture(1)

print("Suppression de la Mercedes terminée")
print("----------------------")


# 3. RECUPERATION + AFFICHAGE

voitures = recuperer_voitures()

print("Liste des voitures dans la base :")

for v in voitures:
    v.afficher_voiture()

print("----------------------")