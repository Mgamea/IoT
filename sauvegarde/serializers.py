from rest_framework import serializers
from .models import Sauvegarde

class SauvegardeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sauvegarde
        fields = ['id', 'nom', 'date_creation', 'chemin', 'taille']
