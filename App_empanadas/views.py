from django.shortcuts import render
from App_empanadas.models import Empanadas
from App_empanadas.forms import Empanada_Form

def crear_productos (request):
    if request.method == "GET":
        context = {
            "form" : Empanada_Form()
        }
        return render (request, "App_empanada/Crear_producto.html", context = context)
    elif request.method == "POST":
        form = Empanada_Form(request.POST)
        if form.is_valid():
            Empanadas.objects.create(
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
                'form': Empanada_Form()
            }
    return render(request, 'App_empanada/Crear_producto.html', context=context)
   
def lista_de_empanadas (request):
    if "Search" in request.GET:
        search = request.GET["Search"]
        los_productos = Empanadas.objects.filter(nombre__contains = search)
    else:
        los_productos = Empanadas.objects.all()
    context = {
        "producto" : los_productos
    }
    return render(request, "App_empanada/lista_de_empanadas.html", context = context)

