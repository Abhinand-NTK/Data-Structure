from django.db import models

# Create your models here.


class Books(models.Model):

    name = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class Store(models.Model):

    name = models.CharField(max_length=20)
    books = models.ManyToManyField(Books)

    def __str__(self):
        return self.name    
