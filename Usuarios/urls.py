from django.contrib.auth.views import LogoutView
from Usuarios.views import Ingreso_a_la_cuenta, registro, actualizacion_de_usuario, actualizar_perfil_de_usuario
from django.urls import path



urlpatterns = [
    path("inicio/", Ingreso_a_la_cuenta, name="inicio" ),
    path("registro/", registro ),
    path('salir/', LogoutView.as_view(template_name = 'Usuarios/salir.html')),
    path("actualizar/", actualizacion_de_usuario ),
    path("actualizacion/", actualizar_perfil_de_usuario ),

]