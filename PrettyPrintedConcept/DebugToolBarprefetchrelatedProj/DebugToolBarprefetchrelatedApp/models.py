from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Store(models.Model):
    name=models.CharField(max_length=100)
    department=models.ManyToManyField(Book)

    def __str__(self):
        return self.name
