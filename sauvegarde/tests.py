from django.test import TestCase

# Create your tests here.
from sauvegarde.models import Sauvegarde
sauvegarde = Sauvegarde.objects.create(humidite=0.5)
print(sauvegarde)

all_sauvegardes = Sauvegarde.objects.all()
for sauvegarde in all_sauvegardes:
    print(sauvegarde)
