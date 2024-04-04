import requests  # Importation de la bibliothèque requests pour effectuer des requêtes HTTP
from .models import Sauvegarde  # Importation du modèle Sauvegarde depuis le fichier models.py de l'application en cours

def envoyer_donnees_vers_thingspeak():
    # Récupération de la dernière sauvegarde enregistrée dans la base de données
    derniere_sauvegarde = Sauvegarde.objects.last()

    # Extraction de la valeur d'humidité de la dernière sauvegarde
    humidite = derniere_sauvegarde._humedite

    # À ce stade, vous devriez avoir la valeur d'humidité que vous souhaitez envoyer à ThingSpeak

    # Code pour envoyer les données à ThingSpeak
    # Voici un exemple de code pour envoyer des données à ThingSpeak:

    url = 'https://api.thingspeak.com/update'
    params = {'api_key': 'VOTRE_CLE_API', 'field1': humidite}
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Données envoyées avec succès à ThingSpeak !")
    else:
        print("Erreur lors de l'envoi des données à ThingSpeak :", response.status_code)
