import mysql.connector
from voiture import Voiture
from crud_db import ajouter_voiture, connecter_db

connexion = None

try:
    connexion = connecter_db()
    print("Connexion réussie !")
except Exception as e:
    print("Erreur de connexion :", e)
finally:
    if connexion is not None:
        connexion.close()

v1 = Voiture("AUDI", "A3", 2025, 60000)
v2 = Voiture("BMW", "M3", 2026, 65000)

ajouter_voiture(v1)
ajouter_voiture(v2)

print("Voiture ajoutée")