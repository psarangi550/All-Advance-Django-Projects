from django.db import models
from django.db.models import Count
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=100)

    def __str__(self):
        return self.ename
