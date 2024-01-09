from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=99)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    reseñas=models.CharField(max_length=99)

class Restaurante(models.Model):
    nombre = models.CharField(max_length=99)
    reseñas = models.FloatField() #quiero que sea el promedio de las reseñas hechas
    descripcion = models.CharField(max_length=250)
    ubicacion=models.CharField(max_length=99)
    instagram = models.URLField()
    #foto=models.ImageField()


class Reseña(models.Model):
    restaurante = models.CharField(max_length=99)
    #reseñas = models.IntegerField()
    estrellas = models.FloatField()
    ubicacion=models.CharField(max_length=99)
    fecha_de_visita = models.DateField()
    fecha_de_reseña = models.DateField()
    reseña=models.CharField(max_length=150)
    #foto=models.ImageField()