from django.db import models

class Production(models.Model):
    
    nom_prod = models.CharField(max_length=100)
    unite_production = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return self.nom_prod