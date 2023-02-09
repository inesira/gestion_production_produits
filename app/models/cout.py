from django.db import models
from django.db import models
from app.models import Production



class Cout(models.Model):
    production = models.ForeignKey(Production, on_delete=models.CASCADE, null=True, blank=True)
    quantite_produite = models.FloatField(null=True, blank=True)
    stock_mp = models.FloatField(null=True, blank=True)
    cout_total_sortie = models.FloatField(null=True, blank=True)
    nombre_depense = models.FloatField(null=True, blank=True)
    cout_total_depense = models.FloatField(null=True, blank=True)
    cout_total_production = models.FloatField(null=True, blank=True)
    quantite_total = models.FloatField(null=True, blank=True)
    cout_production = models.FloatField(null=True, blank=True)
                
     