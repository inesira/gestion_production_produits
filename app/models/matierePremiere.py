from django.db import models

class MatierePremiere(models.Model):
    matiere_premiere = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.matiere_premiere