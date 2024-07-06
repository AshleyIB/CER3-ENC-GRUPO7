from django.shortcuts import render, redirect
import requests
from .models import *
from .forms import FormularioForm
from django.shortcuts import render, redirect


def base(request):
    title = "Inicio"
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = FormularioForm()

    data = {
        "title" : title,
    }

    return render(request, 'core/base.html',data)

def login(request):
    si = 0
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contrasena = request.POST['contraseña']
        nombre_usuario = request.POST['nombre_usuario']
        apellido_usuario = request.POST['apellido_usuario']
        
        try:
            user = Usuario.objects.get(codigo=usuario, contrasena=contrasena, nombre_usuario=nombre_usuario, apellido_usuario=apellido_usuario)
            si = 2 
        except Usuario.DoesNotExist:
            si = 3  

    return render(request, 'core/login.html', {'si': si})

def formulario(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = FormularioForm()

    return render(request, 'core/base.html', {'form': form})
