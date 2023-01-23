from django.urls import path
from App_empanadas.views import lista_de_empanadas, crear_productos

urlpatterns = [
    path("crear/", crear_productos),
    path("listado_de_empanadas/", lista_de_empanadas),
]