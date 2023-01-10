from django.db import models
from app.models import Stock

class Input(models.Model):
    
    matieres_premieres = models.CharField(max_length=45)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateField()
    
   