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

    restaurantes=Restaurante.objects.all()
    return render(request,"AppResto/restaurantes.html",{"restaurantes":restaurantes})

def Reseñas(request):
    return render(request,"AppResto/reseñas.html")



def Crear_Reseñas(request):

    if request.method== "POST":

        formulario= AppResto.forms.Reseña_form(request.POST) #obtiene del formulario
        print(formulario)

        if formulario.is_valid:
            info=formulario.cleaned_data
            reseña_nuevo=Reseña(
                restaurantre=info["restaurantre"],
                estrellas=info["estrellas"],
                ubicacion=info["ubicacion"],
                fecha_de_visita=info["fecha_de_visita"],
                fecha_de_reseña= datetime.datetime.now(),
                #foto=info["foto"],
            )
            reseña_nuevo.save()
            return render(request,"AppResto/reseñas.html")
    else:
        formulario= AppResto.forms.Reseña_form()
        return render(request,"AppResto/crear_reseña.html",{"mi_formu":formulario}) 
    
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
    else:
        formulario= AppResto.forms.Restaurante_form()
        return render(request,"AppResto/crear_resto.html",{"mi_formu":formulario})
    
"""
def buscar_restaurante(request):
    
    if request.method =='GET':
        nombre_pedido= request.GET['pedido']
        resultado_busqueda=Restaurante.objects.filter(nombre_pedido__icontains=nombre_pedido)
        return render(request,"AppResto/buscar_restaurante.html",{"resultado_busqueda":resultado_busqueda})

    else:
        #resultado_busqueda=Restaurante.objects
        return render(request,"AppResto/buscar_restaurante.html")

"""
def buscar_restaurante(request):
    if request.method == 'GET' and 'pedido' in request.GET:
        nombre_pedido = request.GET['pedido']
        resultado_busqueda = Restaurante.objects.filter(nombre__icontains=nombre_pedido)
        
        return render(request, "AppResto/buscar_restaurante.html", {"resultado_busqueda": resultado_busqueda})
    else:
        return render(request, "AppResto/buscar_restaurante.html")
