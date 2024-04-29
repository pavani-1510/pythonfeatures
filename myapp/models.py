from django.db import models
from pyexpat import model


# Create your models here.

class ContactModel(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    comment = models.TextField(max_length=255)
    email = models.EmailField(blank=False)

    class Meta:
        db_table = "contactus"

class User(models.Model):
    username= models.CharField()
    email= models.CharField()
    password=models.CharField()

    class Meta:
        db_table = "User"
