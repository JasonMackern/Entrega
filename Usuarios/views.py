from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from Usuarios.models import Prefil_de_usuario
from Usuarios.form import Registro, Usuario_actulizado, Perfil_de_usuario

def Ingreso_a_la_cuenta(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'Usuarios/inicio.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data.get('username')
            contraceña = form.cleaned_data.get('password')

            usuario = authenticate(username=nombre_de_usuario, password=contraceña)

            if usuario is not None:
                login(request, usuario)
                context = {
                    'mensaje':f'Bienvenido {nombre_de_usuario}!!!'
                }
                return render(request, 'inicio.html', context=context)

        form = AuthenticationForm()
        context ={
            'form':form,
            'errores':'Usuario o contraseña incorrectos!'
        }
        return render(request, 'Usuarios/inicio.html', context=context)

def registro(request):
    if request.method == 'GET':
        form = Registro()
        context ={
            'form':form
        }
        return render(request, 'Usuarios/registro.html', context=context)

    elif request.method == 'POST':
        form = Registro(request.POST)
        if form.is_valid():
            usuario = form.save() 
            Prefil_de_usuario.objects.create(usuario=usuario)
            return redirect('inicio')
        
        context = {
            'errores':form.errors,
            'form':Registro()
        }
        return render(request, 'Usuarios/registro.html', context=context)

@login_required
def actualizacion_de_usuario(request):
    usuario = request.user
    if request.method == 'GET':
        form = Usuario_actulizado(initial = {
            'username':usuario.username,
        })
        context ={
            'form':form
        }
        return render(request, 'Usuarios/actualizar_usuario.html', context=context)

    elif request.method == 'POST':
        form = Usuario_actulizado(request.POST)
        if form.is_valid():
            usuario.nombre_de_usuario = form.cleaned_data.get('nombre_de_usuario')
            usuario.save()
            return redirect('index')
        
        context = {
            'errores':form.errors,
            'form':Registro()
        }
        return render(request, 'Usuarios/actualizar_usurio.html', context=context)

def actualizar_perfil_de_usuario(request):
    user = request.user
    if request.method == 'GET':
        form = Perfil_de_usuario(inicial={
            'telefono':request.user.profile.telefono,
            'fecha_de_naciemiento':request.user.profile.fecha_de_naciemiento,
            'foto_de_perfil':request.user.profile.foto_de_perfil
        })
        context ={
            'form':form
        }
        return render(request, 'Usuarios/actualizar_perfil.html', context=context)

    elif request.method == 'POST':
        form = Perfil_de_usuario(request.POST, request.FILES)
        if form.is_valid():
            user.profile.telefono = form.cleaned_data.get('telefono')
            user.profile.fecha_de_naciemiento = form.cleaned_data.get('fecha_de_naciemiento')
            user.profile.foto_de_perfil = form.cleaned_data.get('foto_de_perfil')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errores':form.errors,
            'form':Perfil_de_usuario()
        }
        return render(request, 'Usuarios/registro.html', context=context)