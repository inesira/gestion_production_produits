from django.db import models

from app.models import Category



class Mains_d_oeuvres(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nombre_ou_quantite = models.FloatField()
    revenu = models.FloatField()
    date = models.DateField()