from django.db import models
from app.models import Stock

class Output(models.Model):
    
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price = models.FloatField()
    date = models.DateField()
   