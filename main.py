from crud_db import connecter_db

conn = connecter_db()
print("Connexion OK")
conn.close()



