
# Create your models here.
import datetime
from django.db import models
from django.contrib import admin
from django.utils import timezone


from django.db import models

class Sauvegarde(models.Model):
    # La valeur d'humidité associée à cette sauvegarde
    humidite = models.FloatField(null=True)

    def __str__(self):
        return f"Humidité: {self.humidite}"


admin.site.register(Sauvegarde)

class Question(models.Model):
    # ...
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
