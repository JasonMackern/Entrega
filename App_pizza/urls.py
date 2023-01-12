from django.urls import path
from App_pizza.views import crear_productos, lista_de_productos

urlpatterns = [
    path("crear/", crear_productos),
    path("listado/", lista_de_productos),
]