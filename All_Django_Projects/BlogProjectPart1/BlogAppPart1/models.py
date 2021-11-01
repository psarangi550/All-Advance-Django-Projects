from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AuthorModel(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog")
    name=models.CharField(max_length=200)
