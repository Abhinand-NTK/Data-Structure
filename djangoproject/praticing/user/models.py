from django.db import models

# Create your models here.

class Manufaturer(models.Model):

    Manufaturer = models.CharField(max_length=20)

class Toy(models.Model):

    name = models.CharField(max_length=20,unique=True)
    Manufaturer = models.ForeignKey(Manufaturer,on_delete= models.CASCADE,blank=True)
