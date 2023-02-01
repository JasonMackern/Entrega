from django.shortcuts import render
from App_empanadas.models import Empanadas
from App_empanadas.forms import Empanada_Form
from django.views.generic import DeleteView, UpdateView

def crear_productos (request):
    if request.method == "GET":
        context = {
            "form" : Empanada_Form()
        }
        return render (request, "App_empanada/Crear_producto.html", context = context)
    elif request.method == "POST":
        form = Empanada_Form(request.POST, request.FILES)
        if form.is_valid():
            Empanadas.objects.create(
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

class Editar_empanada (UpdateView):
    model = Empanadas
    fields = '__all__'
    template_name = 'App_empanada/editar.html'
    success_url = '/App_empanadas/listado_de_empanadas/'
    primary_key = "empanada"

class Borrar_empanada (DeleteView):
    model = Empanadas
    template_name = 'App_empanada/borrar.html'
    success_url = '/App_empanadas/listado_de_empanadas/'
    primary_key = "empanada"