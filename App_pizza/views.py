from django.shortcuts import render
from App_pizza.models import Pizzas
from App_pizza.forms import Pizza_Form

def crear_productos (request):
    if request.method == "GET":
        context = {
            "form" : Pizza_Form()
        }
        return render (request, "App_pizza/Crear_productos.html", context = context)
    elif request.method == "POST":
        form = Pizza_Form(request.POST)
        if form.is_valid():
            Pizzas.objects.create(
                nombre=form.cleaned_data['nombre'],
                precio=form.cleaned_data['precio'],
                stock=form.cleaned_data['stock'],
            )
            context = {
                'mensaje': 'Producto creado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Pizza_Form()
            }
    return render(request, 'App_pizza/Crear_productos.html', context=context)
    
def lista_de_productos (request):
    if "Search" in request.GET:
        search = request.GET["Search"]
        los_productos = Pizzas.objects.filter(nombre__contains = search)
    else:
        los_productos = Pizzas.objects.all()
    context = {
        "producto" : los_productos
    }
    return render(request, "App_pizza/listado_de_pizzas.html", context = context)

