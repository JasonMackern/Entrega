from django.urls import path
from App_empanadas.views import lista_de_empanadas

urlpatterns = [
    path("listado_de_empanadas/", lista_de_empanadas),
]