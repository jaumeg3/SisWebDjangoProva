from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Empresa(models.Model):

    """docstring for ."""
    nom = models.TextField(max_length=50)
    web = models.TextField(max_length=100)


class Sobre(models.Model):

    """docstring fordddddddd"""
    amount = models.IntegerField()
    date = models.DateTimeField()
    concept = models.TextField(max_length=50)
    empresa = models.ForeignKey(Empresa)
    politic = models.ForeignKey(User)

    def __unicode__(self):
        return self.empresa.nom + ":" + str(self.amount) + ":"
        + self.politic.get_username()
