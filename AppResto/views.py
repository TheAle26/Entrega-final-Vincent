from django.shortcuts import render

# Create your views here.
#from django.forms import CartAddProductForm
# Create your views here.

def inicio(request):
    return render(request,"AppResto/inicio.html")


def mi_usuario(request):
    return render(request,"AppResto/usuario.html")

def Restos(request):
    return render(request,"AppResto/restos.html")
