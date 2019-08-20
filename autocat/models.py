from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    birth_country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)