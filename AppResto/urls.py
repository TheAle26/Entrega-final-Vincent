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

    #para actualizar
    path('Actualizar_Restaurante/<restaurante>',views.Actualizar_Restaurante,name='Actualizar_Restaurante'),
    path('select_update_reseña/', views.select_update_Reseña, name='select_update_reseña'),
    path('update_reseña/<int:reseña_id>/', views.update_Reseña, name='update_reseña'),
    

    #para borrar
    path('select_delete_restaurante',views.select_delete_Restaurante,name='select_delete_restaurante'),
    path('delete_restaurante/<restaurante_nombre>/', views.delete_Restaurante, name='delete_restaurante'),

    path('select_delete_reseña/', views.select_delete_Reseña, name='select_delete_reseña'),
    path('delete_reseña/<int:reseña_id>/', views.delete_Reseña, name='delete_reseña'),
    
]