from django.db import models
from app.models import Category
from app.models import Production

class Mains_d_oeuvres(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nombre = models.FloatField()
    revenu = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    production = models.ForeignKey(Production, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()