from django.shortcuts import render, get_object_or_404
from AppResto.models import Restaurante, Reseña
from django.http import HttpResponse
import datetime
import AppResto.forms 

# Create your views here.
#from django.forms import CartAddProductForm
# Create your views here.

def prueba(request):
    return render(request,"AppResto/prueba.html")

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
    
    reseñas=Reseña.objects.all()
    return render(request,"AppResto/reseñas.html",{"reseñas":reseñas})



def Crear_Reseñas(request):

    

    if request.method== "POST":

        formulario= AppResto.forms.Reseña_form(request.POST) #obtiene del formulario
        print(formulario)

        if formulario.is_valid:
            info=formulario.cleaned_data
            reseña_nuevo=Reseña(
                restaurante=info["restaurante"],
                puntuacion=info["puntuacion"],
                ubicacion=info["ubicacion"],
                fecha_de_visita=info["fecha_de_visita"],
                fecha_de_reseña= datetime.datetime.now(),
                reseña=info["reseña"]
                #foto=info["foto"],
            )
            reseña_nuevo.save()
            reseñas=Reseña.objects.all()
            return render(request,"AppResto/reseñas.html",{"reseñas":reseñas})
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
            restaurantes=Restaurante.objects.all()
            return render(request,"AppResto/restaurantes.html",{"restaurantes":restaurantes})
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

def update_Reseña(request, reseña_id):
    reseña_update = get_object_or_404(Reseña, id=reseña_id)

    if request.method == "POST":
        formulario = AppResto.forms.Reseña_form(request.POST)
        if formulario.is_valid():  # Asegúrate de agregar los paréntesis aquí
            info = formulario.cleaned_data

            restaurante_nombre = info["restaurante"].nombre
            reseña_update.restaurante = restaurante_nombre

            reseña_update.puntuacion = info["puntuacion"]
            reseña_update.ubicacion = info["ubicacion"]
            reseña_update.fecha_de_visita = info["fecha_de_visita"]
            reseña_update.fecha_de_reseña = datetime.datetime.now()
            reseña_update.reseña = info["reseña"]

            reseña_update.save()
            reseñas = Reseña.objects.all()

            return render(request, "AppResto/reseñas.html", {"reseñas": reseñas})
    else:
        formulario = AppResto.forms.Reseña_form(initial={
            "restaurante": reseña_update.restaurante,
            "puntuacion": reseña_update.puntuacion,
            "ubicacion": reseña_update.ubicacion,
            "fecha_de_visita": reseña_update.fecha_de_visita,
            "fecha_de_reseña": reseña_update.fecha_de_reseña,
            "reseña": reseña_update.reseña
        })

        return render(request, "AppResto/update_reseña.html", {"mi_formu": formulario})


def select_Reseña(request):
    Reseñas = Reseña.objects.all()
    return render(request, "AppResto/select_reseña.html", {"reseñas":Reseñas})


def update_Restaurante(request, restaurante_id):
    restaurante_update = get_object_or_404(Restaurante, id=restaurante_id)

    if request.method == "POST":
        formulario = AppResto.forms.Reseña_form(request.POST)
        if formulario.is_valid():  # Asegúrate de agregar los paréntesis aquí
            info = formulario.cleaned_data

        
            restaurante_update.nombre = info["nombre"]
            restaurante_update.reseñas = info["reseñas"]
            restaurante_update.descripcion = info["descripcion"]
            restaurante_update.instagram = info["instagram"]
            restaurante_update.ubicacion = info["ubicacion"]

            restaurante_update.save()
            restaurantes = Restaurante.objects.all()

            return render(request, "AppResto/restaurantes.html", {"restaurantes":restaurantes})
    else:
        formulario = AppResto.forms.Restaurante_form(initial={
            "nombre": restaurante_update.nombre,
            "reseñas": restaurante_update.reseñas,
            "descripcion": restaurante_update.descripcion,
            "instagram": restaurante_update.instagram,
            "ubicacion": restaurante_update.ubicacion,
            
        })

        return render(request, "AppResto/update_restaurante.html", {"mi_formu": formulario})


def select_Restaurante(request):
    restaurantes = Restaurante.objects.all()
    return render(request, "AppResto/select_restaurante.html", {"restaurantes":restaurantes})
    
    
#borrar 


def delete_Reseña(request, reseña_id):
    reseña = get_object_or_404(Reseña, id=reseña_id)
    reseña.delete()

    # Recargar la lista de reseñas después de la eliminación
    reseñas = Reseña.objects.all()
    return render(request, "AppResto/reseñas.html", {"reseñas": reseñas})

def delete_Restaurante(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, id=restaurante_id)
    restaurante.delete()

    # Recargar la lista de reseñas después de la eliminación
    restaurantes = Restaurante.objects.all()
    return render(request, "AppResto/restaurantes.html", {"restaurantes": restaurantes})




