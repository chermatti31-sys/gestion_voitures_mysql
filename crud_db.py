import json
import mysql.connector
from voiture import Voiture


# Créer la fonction connecter_db

def connecter_db():
    with open("config.json", "r") as fichier:
        config = json.load(fichier)

    connexion = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )

    return connexion

# Créer la fonction ajouter_voiture

def ajouter_voiture(voiture):
    connexion = connecter_db()
    curseur = connexion.cursor()

    curseur.execute("""
        CREATE TABLE IF NOT EXISTS voiture (
            id INT AUTO_INCREMENT PRIMARY KEY,
            marque VARCHAR(100),
            modele VARCHAR(100),
            annee INT,
            prix DECIMAL(12,2)
        )
    """)

    requete = """
        INSERT INTO voiture (marque, modele, annee, prix)
        VALUES (%s, %s, %s, %s)
    """

    valeurs = (voiture.marque, voiture.modele, voiture.annee, voiture.prix)

    curseur.execute(requete, valeurs)
    connexion.commit()

    curseur.close()
    connexion.close()

# Créer la fonction supprimer_voiture
def supprimer_voiture(id):
    connexion = connecter_db()
    curseur = connexion.cursor()

    curseur.execute("DELETE FROM voiture WHERE id = %s", (id,))
    connexion.commit()

    curseur.close()
    connexion.close()


#Créer la fonction recuperer_voitures()

def recuperer_voitures():
    connexion = connecter_db()
    curseur = connexion.cursor()

    curseur.execute("SELECT id, marque, modele, annee, prix FROM voiture")

    resultats = curseur.fetchall()

    liste = []

    for ligne in resultats:
        voiture = Voiture(ligne[1], ligne[2], ligne[3], ligne[4], ligne[0])
        liste.append(voiture)

    curseur.close()
    connexion.close()

    return liste