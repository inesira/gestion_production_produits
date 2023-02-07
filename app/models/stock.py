from django.db import models
from app.models import Output
from app.models import Input


class Stock(models.Model):
    
    matiere_premieres = models.ForeignKey(Output, on_delete=models.CASCADE, null=True, blank=True)
    entree = models.FloatField()
    sortie = models.FloatField()
    stock_actuel = models.FloatField()
    unite_entree_sortie = models.CharField(max_length=45, null=True, blank=True)
    prix_unitaire = models.FloatField()
    date_entree = models.DateField(null=True, blank=True)
    date_sortie = models.DateField(null=True, blank=True)
    
   