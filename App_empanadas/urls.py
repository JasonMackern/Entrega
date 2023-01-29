from django.urls import path
from App_empanadas.views import lista_de_empanadas, crear_productos, Borrar_empanada, Editar_empanada

urlpatterns = [
    path("crear/", crear_productos),
    path("listado_de_empanadas/", lista_de_empanadas),
    path("editar/<int:pk>/", Editar_empanada.as_view(), name="editar"),
    path("borrar/<int:pk>/", Borrar_empanada.as_view(), name="borrar"),    
]