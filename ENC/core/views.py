from django.shortcuts import render
import requests
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


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
    codigo = request.POST.get("codigo")
    litros = request.POST.get("litros")
    fecha = request.POST.get("fecha")
    turno= request.POST.get("turno")
    hora= request.POST.get("hora")
    operador= request.POST.get("operador")

    nuevo_formulario = Formulario(codigo=codigo, litros=litros, fecha=fecha, turno=turno, hora=hora, operador=operador)
    nuevo_formulario.save()
    return redirect("base")
