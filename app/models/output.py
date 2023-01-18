from django.db import models
from app.models import Stock

class Output(models.Model):
    
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantite = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    total = models.FloatField(null=True, blank=True)
    date = models.DateField()
   