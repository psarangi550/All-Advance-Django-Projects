from django.db import models

# Create your models here.
class Student(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    esal=models.FloatField()
    eaddr=models.TextField()

    def __str__(self):
        return self.ename
