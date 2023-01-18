from django.db import models
from app.models import Stock

class Situation_stock(models.Model):
    
    stocks = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantite = models.FloatField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)