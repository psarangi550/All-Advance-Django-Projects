from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Character(models.Model):
    name=models.CharField(max_length=100)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
