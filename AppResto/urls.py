from django.urls import path
from AppResto import views

urlpatterns=[
    path('inicio/',views.inicio,name="inicio"),
    path('restaurantes/',views.Restaurantes,name="Restos"),
    path('crear_restaurante/',views.Crear_Restaurante, name="crear_restaurante"),  #nuevos datos
    path('crear_reseña/',views.Crear_Reseñas, name="crear_reseña"), #nuevos datos
    path('reseñas/',views.Reseñas,name="reseñas"),
    path('iniciar_sesion/',views.iniciar_sesion, name="iniciar_sesion"),
    path('usuario/',views.mi_usuario, name="usuario"),
    
    #ahora para buscar, me gustaria integrar
    path('buscar_restaurante/',views.buscar_restaurante,name='buscar_restaurante'),
    path('buscar_reseña/',views.buscar_reseña,name='buscar_reseña'),

]