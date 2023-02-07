from django.db import models
from app.models import Input
from app.models import Production
from django.contrib.auth.models import User


class Output(models.Model):
    
    matiere_premiere = models.ForeignKey(Input, on_delete=models.CASCADE, null=True, blank=True)
    quantite_stock = models.FloatField(null=True, blank=True)
    quantite_sortie = models.FloatField(null=True, blank=True)
    unite_sortie = models.CharField(max_length=45, null=True, blank=True)
    priX_unitaire_sortie = models.FloatField(null=True, blank=True)
    prix_total_sortie = models.FloatField(null=True, blank=True)
    date_entree = models.DateField(null=True, blank=True)
    date_sortie = models.DateField(null=True, blank=True)
    production = models.ForeignKey(Production, on_delete=models.CASCADE, null=True, blank=True)
    date_production = models.DateField(null=True, blank=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.matiere_premiere.matiere_Premiere.matiere_premiere