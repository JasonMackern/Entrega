from django.shortcuts import render
from App_gaseosas.models import Gaseosas
from App_gaseosas.forms import Gaseosa_Form
from django.views.generic import DeleteView, UpdateView

def crear_productos (request):
    if request.method == "GET":
        context = {
            "form" : Gaseosa_Form()
        }
        return render (request, "App_gaseosa/Crear_producto.html", context = context)
    elif request.method == "POST":
        form = Gaseosa_Form(request.POST)
        if form.is_valid():
            Gaseosas.objects.create(
                nombre=form.cleaned_data['nombre'],
                precio=form.cleaned_data['precio'],
                stock=form.cleaned_data['stock'],
                imagen=form.cleaned_data['imagen'],
            )
            context = {
                'mensaje': 'Producto creado exitosamente'
            }
        else:
            context = {
                'form_errors': form.errors,
                'form': Gaseosa_Form()
            }
    return render(request, 'App_gaseosa/Crear_producto.html', context=context)
   
def lista_de_gaseosas (request):
    if "Search" in request.GET:
        search = request.GET["Search"]
        los_productos = Gaseosas.objects.filter(nombre__contains = search)
    else:
        los_productos = Gaseosas.objects.all()
    context = {
        "producto" : los_productos
    }
    return render(request, "App_gaseosa/lista_de_gaseosas.html", context = context)

class Editar_gaseosa (UpdateView):
    model = Gaseosas
    fields = '__all__'
    template_name = 'App_gaseosa/editar.html'
    success_url = '/App_gaseosas/listado_de_gaseosas/'
    primary_key = "gaseosa"

class Borrar_gaseosa (DeleteView):
    model = Gaseosas
    template_name = 'App_gaseosa/borrar.html'
    success_url = '/App_gaseosas/listado_de_gaseosas/'
    primary_key = "gaseosa"