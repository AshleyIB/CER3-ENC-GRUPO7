from django.shortcuts import render, redirect
import requests
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
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
        try:
            user = Usuario.objects.get(codigo=usuario, contrasena=contrasena)
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

    return render(request, 'core/formulario.html', {'form': form})
