from django.urls import path
from AppResto import views
from django.contrib.auth.views import LogoutView

urlpatterns=[

    path('login/',views.login_request,name='iniciar_sesion'),
    path('register/',views.register,name='register'),
    path('inicio/',views.inicio,name="inicio"),
    path('restaurantes/',views.Restaurantes,name="Restos"),
    path('crear_restaurante/',views.Crear_Restaurante, name="crear_restaurante"),  #nuevos datos
    path('crear_reseña/',views.Crear_Reseñas, name="crear_reseña"), #nuevos datos
    path('reseñas/',views.Reseñas,name="reseñas"),
    path('user/',views.mi_usuario, name="user"),
    
    #ahora para buscar, me gustaria integrar
    path('buscar_restaurante/',views.buscar_restaurante,name='buscar_restaurante'),
    path('buscar_reseña/',views.buscar_reseña,name='buscar_reseña'),

    #para actualizar
    path('select_reseña/', views.select_Reseña, name='select_reseña'),
    path('update_reseña/<int:reseña_id>/', views.update_Reseña, name='update_reseña'),
    path('select_restaurante/', views.select_Restaurante, name='select_restaurante'),
    path('update_restaurante/<int:restaurante_id>/', views.update_Restaurante, name='update_restaurante'),
    

    #para borrar
    path('delete_restaurante/<int:restaurante_id>/', views.delete_Restaurante, name='delete_restaurante'),

    path('delete_reseña/<int:reseña_id>/', views.delete_Reseña, name='delete_reseña'),
    #prueba
    path('prueba/', views.prueba, name='prueba'),
    path('logout/', LogoutView.as_view(template_name='registro/logout.html'), name='logout'),
    path('edit_Profile/', views.edit_Profile, name='edit_Profile'),
]