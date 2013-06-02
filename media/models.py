from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    date = models.DateField('insert date', default=timezone.now())

    def __unicode__(self):
        return u'{} - {}'.format(self.artist.name, self.name)

