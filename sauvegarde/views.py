
# Create your views here.
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Sauvegarde
from .serializers import SauvegardeSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def recevoir_donnees_humidite(request):
    print("execution de reception de données")
    if request.method == 'POST':  # Vérifie si la requête est de type POST
        print("une demande POST a ete effectuée*****************")
    # Récupère la valeur d'humidité à partir des données POST
        humidite = request.POST.get('humidite') # Supposons que les données d'humidité sont envoyées via POST
        if humidite is not None:
            try:
                humidite = float(humidite)
                sauvegarde = Sauvegarde.objects.create(humidite=humidite)
                return JsonResponse({'message': 'Données d\'humidité sauvegardées avec succès.'}, status=201)
            except ValueError:
                return JsonResponse({'error': 'La valeur d\'humidité doit être un nombre.'}, status=400)
        else:
            return JsonResponse({'error': 'Le champ humidite est requis.'}, status=400)
    else:
        return JsonResponse({'error': 'Cette vue ne prend en charge que les requêtes POST.'}, status=405)

'''
        # Crée une nouvelle instance de Sauvegarde avec la valeur d'humidité reçue
        sauvegarde = Sauvegarde.objects.create(humidite=humidite)
        # Renvoie une réponse JSON indiquant le succès de la création de la sauvegarde et l'ID de la sauvegarde créée
        return JsonResponse({'status': 'success', 'sauvegarde_id': sauvegarde.id})
        # Si la méthode de la requête n'est pas POST, renvoie une réponse JSON d'erreur avec un code d'état 400 (Bad Request)
        return JsonResponse({'status': 'error'}, status=400)
'''

def envoi_donnees_humidite(request):
    payload ={'humidite':"25", 'temperature': "28"}
    url= "http://127.0.0.1:8000/notre-application/"
    x=requests.post(url,json=payload)
    return JsonResponse({'status': True}, status=400)

'''
    sauvegardes = Sauvegarde.objects.all()
    return render(request, 'sauvegarde/liste_sauvegardes.html', {'sauvegardes': sauvegardes})
    '''

class SauvegardeListCreate(generics.ListCreateAPIView):
    queryset = Sauvegarde.objects.all()
    serializer_class = SauvegardeSerializer


# Utilisé pour autoriser les requêtes POST sans jeton CSRF
