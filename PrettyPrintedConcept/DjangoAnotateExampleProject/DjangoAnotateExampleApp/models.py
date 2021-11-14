from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural="countries"

    def __str__(self):
        return self.name

class City(models.Model):
    name=models.CharField(max_length=100)
    population=models.IntegerField(null=True,blank=True)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="cities"

    def __str__(self):
        return self.name


