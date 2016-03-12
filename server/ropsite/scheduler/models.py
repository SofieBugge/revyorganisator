from django.db import models
from time import strftime

#import reader

# Create your models here.

class Øvedage(models.Model):
    dato = models.DateField("Øvedag")
    radmd5 = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.dato.strftime("%Y-%m-%d")


class Lokaler(models.Model):
    lokalenavn = models.CharField(max_length=128, unique=True)
    øvedag = models.ForeignKey("Øvedage", null=True)

    def __str__(self):
        return str(self.lokalenavn)

class Segmenter(models.Model):
    actid      = models.IntegerField(default=0)
    lokale     = models.ForeignKey("Lokaler", null=True)
    start      = models.CharField(max_length=5)
    slut       = models.CharField(max_length=5)
    pre_break  = models.IntegerField(default=15)
    post_break = models.IntegerField(default=15)

    def __str__(self):
        return str(self.actid)
        #return reader.reader(self.actid "title")
