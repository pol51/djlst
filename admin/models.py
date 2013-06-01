from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist)
    date = models.DateField('insert date', auto_now=True)

    def __unicode__(self):
        return u'{} - {}'.format(self.artist.name, self.name)
