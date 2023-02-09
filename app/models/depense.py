from django.db import models
from app.models import Category
from app.models import Production



class Depense(models.Model):
    categorie_depense = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    quantite_depense = models.FloatField(null=True, blank=True)
    prix_unitaire_depense = models.FloatField(null=True, blank=True)
    Prix_total_depense = models.FloatField(null=True, blank=True)
    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    date_depense = models.DateField(null=True, blank=True)
    # date_production = models.DateField(null=True, blank=True)
    # utilisateur = models.CharField(max_length=45, null=True, blank=True)    

     
    

    
    
    