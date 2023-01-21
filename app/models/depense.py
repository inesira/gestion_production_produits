from django.db import models
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
     
    

    
    
    