from django.urls import path
from AppResto import views

urlpatterns=[
    path('inicio',views.inicio,name="inicio"),
    path('catalogo',views.Restos,name="Restos"),
    path('mi_usuario',views.mi_usuario, name="mi_usuario"),

]