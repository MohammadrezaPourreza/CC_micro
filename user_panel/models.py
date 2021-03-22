from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=50,unique=True)
    #token = models.CharField(max_length=300,unique=True)
    name = models.CharField(max_length=20)
    family_name = models.CharField(max_length=30)
    phone_number = models.BigIntegerField()
    email = models.EmailField(max_length=254)

