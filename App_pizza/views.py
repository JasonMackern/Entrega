from django.shortcuts import render
from App_pizza.models import Pizzas
from App_pizza.forms import Pizza_Form

def crear_productos (request):
    if request.method == "GET":
        context = {
            "form" : Pizza_Form()
        }
        return render (request, "Crear_productos.html", context = context)
    elif request.method == "POST":
        Pizzas.objects.create(nombre = request.POST["nombre"], precio = request.POST["precio"])
        return render (request, "Crear_producto.html", context={})
    
def lista_de_productos (request):
    if "Search" in request.GET:
        search = request.GET["Search"]
        los_productos = Pizzas.objects.filter(nombre__contains = search)
    else:
        los_productos = Pizzas.objects.all()
    context = {
        "producto" : los_productos
    }
    return render(request, "listado_de_pizzas.html", context = context)
