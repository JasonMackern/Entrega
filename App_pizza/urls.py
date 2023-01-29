from django.urls import path
from App_pizza.views import crear_productos, lista_de_productos, Borrar_pizza, Editar_pizza

urlpatterns = [
    path("crear/", crear_productos),
    path("listado/", lista_de_productos),
    path("editar/<int:pk>/", Editar_pizza.as_view(), name="editar"),
    path("borrar/<int:pk>/", Borrar_pizza.as_view(), name="borrar"),
]