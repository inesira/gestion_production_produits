from django.db import models
from app.models import Depense
from app.models import Product

class Cout_production(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantite = models.FloatField(null=True, blank=True)
    unite = models.CharField(max_length=45, null=True, blank=True)
    depense = models.ForeignKey(Depense, on_delete=models.CASCADE, null=True, blank=True)
    cout_total_pro =models.FloatField(null=True, blank=True)
    cout_prod =models.FloatField(null=True, blank=True)
    date = models.DateField()
   