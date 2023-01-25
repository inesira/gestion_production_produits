from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adress = models.CharField(max_length=45)
    username = models.CharField(max_length=45,null=True)
    password = models.CharField(max_length=45,null=True)
    
    def __str__(self):
        return self.first_name+", "+self.last_name