from django.shortcuts import render

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
    return render(request,"AppResto/crear_reseña.html")

def Crear_Restaurante(request):
    return render(request,"AppResto/crear_resto.html")