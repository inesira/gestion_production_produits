from django.db import models

class Category(models.Model):
    type_depense = models.CharField(max_length=45, null=True, blank=True)
    
    
    def __str__(self):
        return self.type_depense
    