from django.db import models
from datetime import datetime

# Create your models here.

class Reseñador(models.Model):
    usuario = models.CharField(max_length=99)
    password = models.CharField(max_length=20)
    email = models.EmailField()

class Resto(models.Model):
    nombre = models.CharField(max_length=99)
    reseñas = models.FloatField(max_length=5)
    descripcion = models.CharField(max_length=250)
    ubicacion=models.CharField(max_length=99)
    instagram = models.URLField()


class Reseña(models.Model):
    restaurantre = models.CharField(max_length=99)
    reseñas = models.FloatField(max_length=5)
    estrellas = models.FloatField(max_length=250)
    ubicacion=models.CharField(max_length=99)
    fecha_de_visita = models.DateField()
    fecha_de_reseña = models.DateField(datetime.now())