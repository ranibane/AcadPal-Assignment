from django.db import models
from rest_framework.pagination import PageNumberPagination
# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=70, blank=False, default='', unique = True)
    description = models.CharField(max_length=200,blank=False, default='')
    population = models.IntegerField(blank=False)
    gdp = models.FloatField(blank=False)

class State(models.Model):
    name = models.CharField(max_length=70, blank=False, default='', unique = True)
    description = models.CharField(max_length=200,blank=False, default='')
    population = models.IntegerField(blank=False)
    gdp = models.FloatField(blank=False, default='')
    country = models.ForeignKey(Country, on_delete = models.CASCADE)

class City(models.Model):
    name = models.CharField(max_length=70, blank=False, default='', unique = True)
    description = models.CharField(max_length=200,blank=False, default='')
    population = models.IntegerField(blank=False)
    gdp = models.FloatField(blank=False, default='')
    state = models.ForeignKey(State, on_delete = models.CASCADE)

class Person(models.Model):
    fname = models.CharField(max_length=70, blank=False, default='', unique = True)
    mname = models.CharField(max_length=70, blank=False, default='', unique = True)
    lname = models.CharField(max_length=70, blank=False, default='', unique = True)
    city = models.ForeignKey(City, on_delete = models.CASCADE)