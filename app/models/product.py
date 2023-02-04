from django.db import models

class Product(models.Model):
    type_produit = models.CharField(max_length=100, null=True,blank=True)
    
    def __str__(self):
        return self.type_produit