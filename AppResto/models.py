from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=99)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    reseñas=models.CharField(max_length=99)

class Restaurante(models.Model):
    nombre = models.CharField(max_length=99)
    reseñas = models.ValueRange(start=0,end=5) #quiero que sea el promedio de las reseñas hechas
    descripcion = models.CharField(max_length=250)
    ubicacion=models.CharField(max_length=99)
    instagram = models.URLField()
    foto=models.ImageField()


class Reseña(models.Model):
    restaurantre = models.CharField(max_length=99)
    #reseñas = models.ValueRange(start=0,end=5)
    estrellas = models.ValueRange(start=0,end=5)
    ubicacion=models.CharField(max_length=99)
    fecha_de_visita = models.DateField()
    fecha_de_reseña = models.DateField()
    foto=models.ImageField()