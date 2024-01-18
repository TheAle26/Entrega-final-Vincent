from django.db import models

# Create your models here.


"""
class Restaurante(models.Model):
    nombre = models.CharField(max_length=99)
    calificacion = models.FloatField() #quiero que sea el promedio de las reseñas hechas
    descripcion = models.CharField(max_length=250)
    ubicacion=models.CharField(max_length=99)
    instagram = models.URLField()
    foto = models.ImageField(upload_to='AppResto/img/')
    usuario=models.CharField(max_length=150)

    def __str__(self):
        return self.nombre



class Reseña(models.Model):
    restaurante = models.CharField(max_length=99)
    #reseñas = models.IntegerField()
    puntuacion = models.FloatField()
    ubicacion=models.CharField(max_length=99)
    fecha_de_visita = models.DateField()
    fecha_de_reseña = models.DateField()
    reseña=models.CharField(max_length=150)
    foto = models.ImageField(upload_to='AppResto/img/')
    usuario=models.CharField(max_length=150)

    def __str__(self):
        return f"Reseña de {self.restaurante}"

class Usuario(models.Model):
    usuario = models.CharField(max_length=99)
    password = models.CharField(max_length=20)
    email = models.EmailField()

     """

from django.db.models import Avg


class Restaurante(models.Model):
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=250)
    ubicacion = models.CharField(max_length=99)
    instagram = models.URLField()
    foto = models.ImageField(upload_to='AppResto/img/')
    usuario = models.CharField(max_length=150)
    calificacion = models.FloatField(default=0.0)  # Por defecto, la calificación comienza en 0.0

    def actualizar_calificacion(self):
        # Obtén el promedio de las puntuaciones de las reseñas asociadas a este restaurante
        promedio_puntuaciones = Reseña.objects.filter(restaurante=self).aggregate(Avg('puntuacion'))['puntuacion__avg']
        
        # Si hay reseñas, actualiza la calificación del restaurante
        if promedio_puntuaciones is not None:
            self.calificacion = round(promedio_puntuaciones, 2)
            self.save()

    def __str__(self):
        return self.nombre

class Reseña(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    puntuacion = models.FloatField()
    #ubicacion = models.CharField(max_length=99)
    fecha_de_visita = models.DateField()
    fecha_de_reseña = models.DateField(auto_now_add=True)
    reseña = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='AppResto/img/')
    usuario = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Llama a la función para actualizar la calificación del restaurante
        self.restaurante.actualizar_calificacion()

    def __str__(self):
        return f"Reseña de {self.restaurante.nombre}"

    
class User(models.Model):
    # ... otros campos ...
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=150)

    # ... otras configuraciones ...
