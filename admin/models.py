from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)

class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    date = models.DateField('insert date')
