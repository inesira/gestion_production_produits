from django.db import models
<<<<<<< HEAD
from app.models import Production

class Depense(models.Model):
    
    type_depense =models.CharField(max_length=100, null=True, blank=True)
    production= models.ForeignKey(Production, on_delete=models.CASCADE)
    stocks = models.IntegerField(null=True, blank=True)
    cout_total_sorties = models.FloatField(null=True, blank=True)
    categories = models.IntegerField(null=True, blank=True)
    cout_total_m = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.type_depense    
=======
from app.models import Category
from app.models import Production



class Depense(models.Model):
    categorie_depense = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    quantite_depense = models.FloatField(null=True, blank=True)
    prix_unitaire_depense = models.FloatField(null=True, blank=True)
    Prix_total_depense = models.FloatField(null=True, blank=True)
    production = models.ForeignKey(Production, on_delete=models.CASCADE)
    date_depense = models.DateField(null=True, blank=True)
    date_production = models.DateField(null=True, blank=True)
    utilisateur = models.CharField(max_length=45, null=True, blank=True)    
>>>>>>> feature/data_modeling_update
     
    

    
    
    