from django import forms

class Restaurante_form(forms.Form):
    nombre = forms.CharField(max_length=99)
    reseñas = forms.FloatField(min_value=0,max_value=5) #quiero que sea el promedio de las reseñas hechas
    descripcion = forms.CharField(max_length=250)
    ubicacion=forms.CharField(max_length=99)
    instagram = forms.URLField()
    #foto=forms.ImageField()

class Reseña_form(forms.Form):
    restaurantre = forms.CharField(max_length=99) #quiero que sea una lista despegable de los que ya existen
    estrellas = forms.FloatField(min_value=0,max_value=5) 
    ubicacion = forms.CharField(max_length=250)
    fecha_de_visita=forms.CharField(max_length=99)
    fecha_de_reseña = forms.URLField()
    #foto=forms.ImageField() 

