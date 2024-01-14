from django.shortcuts import render, get_object_or_404, redirect
from AppResto.models import Restaurante, Reseña
from django.http import HttpResponse, HttpResponseBadRequest
import datetime
import AppResto.forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.
#from django.forms import CartAddProductForm
# Create your views here.

def prueba(request):
    return render(request,"AppResto/prueba.html")



def iniciar_sesion(request):
    return render(request,"AppResto/iniciar_sesion.html")

def mi_usuario(request):
    return render(request,"AppResto/user.html")

def crear_usuario(request):
    return render(request,"AppResto/crear_usuario.html")

def Restaurantes(request):

    restaurantes=Restaurante.objects.all()
    return render(request,"AppResto/restaurantes.html",{"restaurantes":restaurantes})

def Reseñas(request):
    
    reseñas=Reseña.objects.all()
    return render(request,"AppResto/reseñas.html",{"reseñas":reseñas})


def Crear_Reseñas(request):
    if request.method == "POST":
        formulario = AppResto.forms.Reseña_form(request.POST, request.FILES)

        if formulario.is_valid():
            # Extraemos los datos del formulario
            info = formulario.cleaned_data

            # Creamos una instancia de reseña y asignamos los valores !!!
            reseña_nuevo = Reseña(
                restaurante=info["restaurante"],
                puntuacion=info["puntuacion"],
                ubicacion=info["ubicacion"],
                fecha_de_visita=info["fecha_de_visita"],
                fecha_de_reseña = datetime.datetime.now(),
                reseña=info["reseña"],
                foto=info["foto"],
            )

            # Guardamos la instancia del restaurante
            reseña_nuevo.save()

            # Recargamos la lista de restaurantes después de la creación
            reseñas = Reseña.objects.all()

          
            return render(request, "AppResto/reseñas.html", {"reseñas": reseñas})
        else:
            mensaje="Formulario no valido"
            formulario = AppResto.forms.Reseña_form()
            return render(request, "AppResto/crear_reseña.html", {"mi_formu": formulario,'mensaje':mensaje})

    else:
        formulario = AppResto.forms.Reseña_form()

        return render(request, "AppResto/crear_reseña.html", {"mi_formu": formulario})

    
def Crear_Restaurante(request):
    if request.method == "POST":
        formulario = AppResto.forms.Restaurante_form(request.POST, request.FILES)

        if formulario.is_valid():
            # Extraemos los datos del formulario
            info = formulario.cleaned_data

            # Creamos una instancia de Restaurante y asignamos los valores
            resto_nuevo = Restaurante(
                nombre=info["nombre"],
                calificacion=info["calificacion"],
                descripcion=info["descripcion"],
                ubicacion=info["ubicacion"],
                instagram=info["instagram"],
                foto=info["foto"],
            )

            # Guardamos la instancia del restaurante
            resto_nuevo.save()

            # Recargamos la lista de restaurantes después de la creación
            

            return redirect('Restos') #Es el nombre de la view: name="nombre"
    else:
        formulario = AppResto.forms.Restaurante_form()

        return render(request, "AppResto/crear_resto.html", {"mi_formu": formulario})
    

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
        if formulario.is_valid():
            info = formulario.cleaned_data

            restaurante_nombre = info["restaurante"].nombre
            reseña_update.restaurante = restaurante_nombre

            reseña_update.puntuacion = info["puntuacion"]
            reseña_update.ubicacion = info["ubicacion"]
            reseña_update.fecha_de_visita = info["fecha_de_visita"]
            reseña_update.fecha_de_reseña = datetime.datetime.now()
            reseña_update.reseña = info["reseña"]

            foto = request.FILES.get('foto')
            if foto:
                reseña_update.foto = foto

            reseña_update.save()
            reseñas = Reseña.objects.all()

            return render(request, "AppResto/reseñas.html", {"reseñas": reseñas})
        else:
            # Manejar el caso en que el formulario no es válido
            print(formulario.errors)
            return HttpResponseBadRequest("El formulario no es válido. Revise los datos proporcionados.")
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
        formulario = AppResto.forms.Restaurante_form(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data

            restaurante_update.nombre = info["nombre"]
            restaurante_update.calificacion = info["calificacion"]
            restaurante_update.descripcion = info["descripcion"]
            restaurante_update.instagram = info["instagram"]
            restaurante_update.ubicacion = info["ubicacion"]
            
            # Actualizamos la foto solo si se proporciona una nueva
            foto = request.FILES.get('foto')
            if foto:
                restaurante_update.foto = foto

            restaurante_update.save()
            
            # Recargamos la lista de restaurantes después de la actualización
            restaurantes = Restaurante.objects.all()

            return render(request, "AppResto/restaurantes.html", {"restaurantes": restaurantes})
    else:
        formulario = AppResto.forms.Restaurante_form(initial={
            "nombre": restaurante_update.nombre,
            "reseñas": restaurante_update.reseñas,
            "descripcion": restaurante_update.descripcion,
            "instagram": restaurante_update.instagram,
            "ubicacion": restaurante_update.ubicacion,
            # No incluimos la foto aquí, ya que se manejará en el formulario de POST
        })

    return render(request, "AppResto/update_restaurante.html", {"mi_formu": formulario})

def select_Restaurante(request):
    restaurantes = Restaurante.objects.all()
    return render(request, "AppResto/select_restaurante.html", {"restaurantes":restaurantes})
    
#para borrar 

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


#login y logout



'''
def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            authenticated_user = authenticate(username=user.username, password=request.POST['password1'])

            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('inicio')  # Redirect to the appropriate URL after login
            else:
                mensaje = "Credenciales incorrectas"
        else:
            mensaje = "Credenciales incorrectas"
    else:
        formulario = AuthenticationForm()
        mensaje = ""

    return render(request, "registro/login.html", {"formulario": formulario, 'mensaje': mensaje})

'''
def register(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            user = formulario.save()
            authenticated_user = authenticate(username=user.username, password=request.POST['password1'],)

            if authenticated_user is not None:
                login(request, authenticated_user)
                return render(request,'AppResto/inicio.html',{'mensaje':f'Bienvenido al sitio f{user}!'})  # Redirect to the appropriate URL after registration

    else:
        formulario = UserCreationForm()

    return render(request, "registro/register.html", {"formulario": formulario})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username= username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "AppResto/inicio.html", {'mensaje':f'Bienvenido al sitio {username}!'})
            else:
                return render(request, "registro/login.html", {"mensaje":"Datos incorrectos"})
           
        else:
            formulario = AuthenticationForm()
            return render(request, "registro/login.html", {"mensaje":"Formulario erroneo","formulario": formulario})

    formulario = AuthenticationForm()

    return render(request, "registro/login.html", {"formulario": formulario})

'''
def regiser(request):
    if request.method=='POST':

        formulario=UserCreationForm(request.POST)

        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render(request,'AppResto/inicio.html',{'mensaje':f'Bienvenido al sitio f{username}!'})
    
    else:
        formulario=UserCreationForm()
    return render (request,"registro/register.html",{"formulario":formulario})
    '''

def inicio(request):
    
    return render(request,"AppResto/inicio.html")