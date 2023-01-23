from django.urls import path
from App_gaseosas.views import lista_de_gaseosas, crear_productos

urlpatterns = [
    path("crear/", crear_productos),
    path("listado_de_gaseosas/", lista_de_gaseosas),
]