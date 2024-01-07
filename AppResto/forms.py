from django import forms

class Restaurante_form(forms.forms):
    nombre = forms.CharField(max_length=99)
    reseñas = forms.ValueRange(start=0,end=5) #quiero que sea el promedio de las reseñas hechas
    descripcion = forms.CharField(max_length=250)
    ubicacion=forms.CharField(max_length=99)
    instagram = forms.URLField()
    foto=forms.ImageField()