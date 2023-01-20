from django.db import models

class Product(models.Model):
    
    produit = models.CharField(max_length=100)
    quantite = models.FloatField(null=True, blank=True)
    unite_production = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.produit    
  