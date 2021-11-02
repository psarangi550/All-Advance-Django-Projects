from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=200)
    email=models.EmailField(max_length=200,default="",null=True)
