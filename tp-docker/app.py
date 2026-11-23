import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client.test_database 


@app.route("/")
def hello():
  try:
    db.command("ping")
    db_status = "Connexion à MongoDB réussie !"
  except Exception as e:
    db_status = f"Erreur de connexion à MongoDB : {e}"

  return f"Hello, World! Statut de la BDD : {db_status}"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)