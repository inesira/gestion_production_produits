from django.db import models
from app.models import MatierePremiere

class Input(models.Model):
    
<<<<<<< HEAD
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantite = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    total = models.FloatField(null=True, blank=True)
    date = models.DateField()
    
   
=======
    matiere_Premiere = models.ForeignKey(MatierePremiere, on_delete=models.CASCADE,null=True, blank=True)
    quantite_entree = models.FloatField(null=True, blank=True)
    unite_entree = models.CharField(max_length=45, null=True, blank=True)
    prix_unitaire_entree = models.FloatField(null=True, blank=True)
    date_entree = models.DateField(null=True, blank=True)
    utilisateur = models.CharField(max_length=150, null=True, blank=True )

    def __str__(self):
        return self.matiere_Premiere.matiere_premiere
>>>>>>> feature/data_modeling_update
