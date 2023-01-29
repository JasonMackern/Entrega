from django.urls import path
from App_gaseosas.views import lista_de_gaseosas, crear_productos, Borrar_gaseosa, Editar_gaseosa

urlpatterns = [
    path("crear/", crear_productos),
    path("listado_de_gaseosas/", lista_de_gaseosas),
    path("editar/<int:pk>/", Editar_gaseosa.as_view(), name="editar"),
    path("borrar/<int:pk>/", Borrar_gaseosa.as_view(), name="borrar"),
]