from django.shortcuts import render, redirect
import requests
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .forms import FormularioForm


def base(request):
    title = "Inicio"

    data = {
        "title" : title,
    }

    return render(request, 'core/base.html',data)

def login(request):
    tipo_usuario = "invitado"
    users = Usuario.objects.all()
    codigo = request.POST.get('codigo')
    contraseña = request.POST.get('contraseña')
    logeado = 1
    if (codigo != None) and (contraseña!=None):
        logeado = 3

    for usuario in users:
        if usuario.codigo == codigo:
            if contraseña == usuario.contrasena:
                tipo_usuario = usuario.tipo_usuario
                logeado = 2

    data={
        "Usuarios":users,
        "con":contraseña,
        "codigo":codigo,
        "si":logeado,
        "tipo": tipo_usuario,
    }
    return render(request,'core/base.html', data)

def formulario(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = FormularioForm()

    return render(request, 'core/formulario.html', {'form': form})
