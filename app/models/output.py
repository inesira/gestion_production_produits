from django.db import models
from app.models import Stock
from app.models import Production

class Output(models.Model):
    
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantite = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    total = models.FloatField(null=True, blank=True)
    production = models.ForeignKey(Production, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
   