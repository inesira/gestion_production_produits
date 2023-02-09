from django.db import models

class Product(models.Model):
<<<<<<< HEAD
    
    produit = models.CharField(max_length=100,null=True, blank=True)
    quantite = models.FloatField(null=True, blank=True)
    unite_production = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.produit    
  
=======
    type_produit = models.CharField(max_length=100, null=True,blank=True)
    
    def __str__(self):
        return self.type_produit
>>>>>>> feature/data_modeling_update
