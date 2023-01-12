from django.urls import path
from App_gaseosas.views import lista_de_gaseosas

urlpatterns = [
    path("listado_de_gaseosas/", lista_de_gaseosas),
]