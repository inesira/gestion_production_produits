from django.db import models
from app.models import Input


class Output(models.Model):
    
    matiere_premiere = models.ForeignKey(Input, on_delete=models.CASCADE, null=True, blank=True)
    quantite_stock = models.FloatField(null=True, blank=True)
    quantite_sortie = models.FloatField(null=True, blank=True)
    unite_sortie = models.CharField(max_length=45, null=True, blank=True)
    priX_unitaire_sortie = models.FloatField(null=True, blank=True)
    prix_total_sortie = models.FloatField(null=True, blank=True)
    date_sortie = models.DateField(null=True, blank=True)
    utilisateur = models.CharField(max_length=45, blank=True, null=True)