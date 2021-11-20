from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    tittle=models.CharField(max_length=100)
    desc=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle

