import json
import mysql.connector

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