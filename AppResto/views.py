from django.shortcuts import render
from AppResto.models import Restaurante, Reseña
from django.http import HttpResponse
import datetime
import AppResto.forms 
# Create your views here.
#from django.forms import CartAddProductForm
# Create your views here.

def inicio(request):
    return render(request,"AppResto/inicio.html")

def iniciar_sesion(request):
    return render(request,"AppResto/iniciar_sesion.html")

def mi_usuario(request):
    return render(request,"AppResto/usuario.html")

def crear_usuario(request):
    return render(request,"AppResto/crear_usuario.html")

def Restaurantes(request):
    return render(request,"AppResto/restaurantes.html")

def Reseñas(request):
    return render(request,"AppResto/reseñas.html")

def Crear_Reseñas(request):
    if request.method== "POST":
        reseña_nueva= Reseña(
            restaurantre=request.POST["restaurantre"],
            estrellas=request.POST["estrellas"],
            ubicacion=request.POST["ubicacion"],
            fecha_de_visita=request.POST["fecha_de_visita"],
            fecha_de_reseña= datetime.datetime.now(),
            foto=request.POST["foto"])
        reseña_nueva.save()

    return render(request,"AppResto/crear_reseña.html")

def Crear_Restaurante(request):

    if request.method== "POST":
        formulario= AppResto.forms.Restaurante_form(request.POST) #obtiene del formulario
        print(formulario)
        if formulario.is_valid:
            info=formulario.cleaned_data
            resto_nuevo=Restaurante(
                nombre=info["nombre"],
                reseñas=info["reseñas"],
                descripcion=info["descripcion"],
                ubicacion=info["ubicacion"],
                instagram=info["instagram"],
                #foto=info["foto"],
            )
            resto_nuevo.save()
            return render(request,"AppResto/restaurantes.html")
#minutio 50
    else:
        formulario= AppResto.forms.Restaurante_form()
        return render(request,"AppResto/crear_resto.html",{"mi_formu":formulario})