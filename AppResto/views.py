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
    
    Reseñas=Reseña.objects.all()
    return render(request,"AppResto/reseñas.html",{"reseñas":Reseñas})



def Crear_Reseñas(request):

    

    if request.method== "POST":

        formulario= AppResto.forms.Reseña_form(request.POST) #obtiene del formulario
        print(formulario)

        if formulario.is_valid:
            info=formulario.cleaned_data
            reseña_nuevo=Reseña(
                restaurante=info["restaurante"],
                puntuacion=info["estrellas"],
                ubicacion=info["ubicacion"],
                fecha_de_visita=info["fecha_de_visita"],
                fecha_de_reseña= datetime.datetime.now(),
                reseña=info["reseña"]
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
    

def buscar_restaurante(request):

    nombres_restaurantes = Restaurante.objects.values_list('nombre', flat=True)    
    formulario= AppResto.forms.Reseña_form(request.POST) #obtiene del formulario
    if request.method == 'GET' and 'pedido' in request.GET:
        nombre_pedido = request.GET['pedido']
        resultado_busqueda = Restaurante.objects.filter(nombre__icontains=nombre_pedido)
        
        return render(request, "AppResto/buscar_restaurante.html", {"resultado_busqueda": resultado_busqueda,"nombres_restaurantes":nombres_restaurantes})
    else:
        return render(request, "AppResto/buscar_restaurante.html",{"nombres_restaurantes":nombres_restaurantes})
    

def buscar_reseña(request):

    nombres_restaurantes = Restaurante.objects.values_list('nombre', flat=True) 

    if request.method == 'GET' and 'pedido' in request.GET:
        restaurante_pedido = request.GET['pedido']
        resultado_busqueda = Reseña.objects.filter(restaurante__icontains=restaurante_pedido)
        
        return render(request, "AppResto/buscar_reseña.html", {"resultado_busqueda": resultado_busqueda,"nombres_restaurantes":nombres_restaurantes})
    else:
        return render(request, "AppResto/buscar_reseña.html",{"nombres_restaurantes":nombres_restaurantes})
    


#aca para update
    
""""
def Actualizar_Reseñas(request,Reseña):

    #cual actualizo? como hago?
    a=Reseña.reseña
    cual= Reseña.objects.filter(Reseña__reseña=a)
        

    if request.method== "POST":

        formulario= AppResto.forms.Reseña_form(request.POST) #obtiene del formulario
        print(formulario)

        if formulario.is_valid:
            info=formulario.cleaned_data
            reseña_nuevo=Reseña(
                restaurante=info["restaurante"],
                puntuacion=info["estrellas"],
                ubicacion=info["ubicacion"],
                fecha_de_visita=info["fecha_de_visita"],
                fecha_de_reseña= datetime.datetime.now(),
                reseña=info["reseña"]
                #foto=info["foto"],
            )
            reseña_nuevo.save()
            return render(request,"AppResto/reseñas.html")
    else:
        formulario= AppResto.forms.Reseña_form()
        return render(request,"AppResto/crear_reseña.html",{"mi_formu":formulario}) 
"""
def Actualizar_Restaurante(request,Restaurante_nombre):


    restaurante_elegido=Restaurante.objects.get(nombre=Restaurante_nombre)

    if request.method== "POST":

        formulario= AppResto.forms.Restaurante_form(request.POST) #obtiene del formulario
        print(formulario)

        if formulario.is_valid:
            info=formulario.cleaned_data
            
            restaurante_elegido.nombre=info["nombre"],
            restaurante_elegido.reseñas=info["reseñas"],
            restaurante_elegido.descripcion=info["descripcion"],
            restaurante_elegido.ubicacion=info["ubicacion"],
            restaurante_elegido.instagram=info["instagram"],
            #foto=info["foto"],
            
            restaurante_elegido.save()
            return render(request,"AppResto/restaurantes.html")
    else:
        formulario= AppResto.forms.Restaurante_form(initial={"nombre":restaurante_elegido.nombre,"reseñas":restaurante_elegido.reseñas,"descripcion":restaurante_elegido.descripcion,"ubicacion":restaurante_elegido.ubicacion,"instagram":restaurante_elegido.instagram})
       
        return render(request,"AppResto/update_restaurante.html",{"mi_formu":formulario})
