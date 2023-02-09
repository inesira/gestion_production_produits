from django.db import models
<<<<<<< HEAD
from app.models import Stock
from app.models import Production

class Output(models.Model):
    
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantite = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    total = models.FloatField(null=True, blank=True)
    production = models.ForeignKey(Production, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
   
=======
from app.models import Input
from app.models import Production


class Output(models.Model):
    
    matiere_premiere = models.ForeignKey(Input, on_delete=models.CASCADE, null=True, blank=True)
    quantite_stock = models.FloatField(null=True, blank=True)
    quantite_sortie = models.FloatField(null=True, blank=True)
    unite_sortie = models.CharField(max_length=45, null=True, blank=True)
    priX_unitaire_sortie = models.FloatField(null=True, blank=True)
    prix_total_sortie = models.FloatField(null=True, blank=True)
    # date_entree = models.DateField(null=True, blank=True)
    date_sortie = models.DateField(null=True, blank=True)
    production = models.ForeignKey(Production, on_delete=models.CASCADE, null=True, blank=True)
    # date_production = models.DateField(null=True, blank=True)
    # utilisateur = models.CharField(max_length=45, null=True, blank=True)
    
    def __str__(self):
        return self.matiere_premiere.matiere_Premiere.matiere_premiere
>>>>>>> feature/data_modeling_update
