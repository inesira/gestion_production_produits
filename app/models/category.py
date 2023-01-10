from django.db import models
class Category(models.Model):
    nom_categorie = models.CharField(max_length=45)
    revenu = models.FloatField()
    
    def __str__(self):
        return self.nom_categorie
    