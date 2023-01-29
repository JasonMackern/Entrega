from django.shortcuts import render
from django.views.generic import ListView
from inicio.models import Inicio

class Listado (ListView):
    model = Inicio
    template_name = 'inicio.html'
