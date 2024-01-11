from django import forms
from .models import Restaurante

class Restaurante_form(forms.Form):
    nombre = forms.CharField(max_length=99)
    reseñas = forms.FloatField(min_value=0,max_value=5) #quiero que sea el promedio de las reseñas hechas
    descripcion = forms.CharField(max_length=250)
    ubicacion=forms.CharField(max_length=99)
    instagram = forms.URLField()
    foto=forms.ImageField()
    
    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto:
            # Aquí puedes agregar validaciones adicionales para la imagen si es necesario
            pass
        return foto

class Reseña_form(forms.Form):
    restaurante = forms.ModelChoiceField(queryset=Restaurante.objects.all(), empty_label=None, to_field_name="nombre", widget=forms.Select(attrs={'class': 'form-control'})) #quiero que sea una lista despegable de los que ya existen
    puntuacion = forms.FloatField(min_value=0,max_value=5) 
    ubicacion = forms.CharField(max_length=250)
    fecha_de_visita=forms.DateField()
    reseña=forms.CharField(max_length=150)
    foto=forms.ImageField()

    def clean_foto(self):
        foto = self.cleaned_data.get('foto')
        if foto:
            # Aquí puedes agregar validaciones adicionales para la imagen si es necesario
            pass
        return foto

