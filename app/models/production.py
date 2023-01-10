from django.db import models
from app.models import Stock
from app.models import Category



class Production(models.Model):
    
    produit_finis = models.CharField(max_length=100)
    quantite_produite = models.FloatField()
    unite_production = models.FloatField()
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cout_production = models.FloatField()
   
    date = models.DateField()
    
    def __str__(self):
        return self.produit_finis + "" + self.cout_production