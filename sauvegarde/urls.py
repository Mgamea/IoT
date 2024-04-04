from django.urls import path
from .views import SauvegardeListCreate
from . import views

urlpatterns = [
    path("", views.recevoir_donnees_humidite, name="recevoir_donnees_humidite"),
    path("envoie",views.envoi_donnees_humidite, name="envoi_donnees_humidite"),    
    path('api/sauvegardes/', SauvegardeListCreate.as_view(), name='sauvegarde-list-create'),
]
