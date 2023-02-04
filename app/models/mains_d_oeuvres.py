from django.db import models


class Mains_d_oeuvres(models.Model):
    
    nombre = models.FloatField()
    revenu = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    
    date = models.DateField()