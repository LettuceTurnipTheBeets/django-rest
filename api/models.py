from django.db import models


class Animal(models.Model):
    """Animal model"""
    commonName = models.CharField(max_length=20)
    scientificName = models.CharField(max_length=50)
    family = models.CharField(max_length=20)
    imageURL = models.URLField(max_length=200)
