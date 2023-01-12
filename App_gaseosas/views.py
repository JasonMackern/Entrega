from django.shortcuts import render
from App_gaseosas.models import Gaseosas
    
def lista_de_gaseosas (request):
    if "Search" in request.GET:
        search = request.GET["Search"]
        los_productos = Gaseosas.objects.filter(nombre__contains = search)
    else:
        los_productos = Gaseosas.objects.all()
    context = {
        "producto" : los_productos
    }
    return render(request, "lista_de_gaseosas.html", context = context)
