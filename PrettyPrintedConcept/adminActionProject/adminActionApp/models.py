from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    is_passed=models.BooleanField(default=True)
    class Meta:
        verbose_name = "Student"
        verbose_name_plural= "Students"

    def __str__(self):
        return self.name
