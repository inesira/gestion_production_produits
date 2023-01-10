from django.db import models


class Stock(models.Model):
    
    matieres_premieres = models.CharField(max_length=100)
    entrees = models.FloatField()
    sorties = models.FloatField()
    stock_actuel = models.FloatField()
    unite_entrees_sorties = models.CharField(max_length=45)
    prix_unitaire = models.FloatField()
    date = models.DateField()
    
    def __str__(self):
        return self.stock_actuel