from django.db import models
<<<<<<< HEAD

class Production(models.Model):
    
    nom_prod = models.CharField(max_length=100)
    unite_production = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return self.nom_prod
=======
from app.models import Product
# from app.models import Cout

class Production(models.Model):
    
    produit_fini = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantite_produite = models.FloatField(null=True, blank=True)
    unite_production = models.CharField(max_length=100, null=True, blank=True)
    date_production = models.DateField(null=True, blank=True)
    utilisateur = models.CharField(max_length=150, null=True, blank=True)
    # cout = models.ForeignKey(Cout, on_delete=models.CASCADE, null=True, blank=True)
    # cout_totat_production = models.FloatField(null=True, blank=True)
    cout_production =models.FloatField(null=True, blank=True)
    
    
    def __str__(self):
        return self.produit_fini.type_produit
>>>>>>> feature/data_modeling_update
