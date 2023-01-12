from django.shortcuts import render
from App_empanadas.models import Empanadas

    
def lista_de_empanadas (request):
    if "Search" in request.GET:
        search = request.GET["Search"]
        los_productos = Empanadas.objects.filter(nombre__contains = search)
    else:
        los_productos = Empanadas.objects.all()
    context = {
        "producto" : los_productos
    }
    return render(request, "lista_de_empanadas.html", context = context)
# Create your views here.
