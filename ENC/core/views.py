from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import *
from .forms import FormularioForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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

@login_required
def listar_registros(request):
    registros = Formulario.objects.filter(operador=request.user)
    return render(request, 'listar_registros.html', {'registros': registros})

@login_required
def modificar_registro(request, pk):
    registro = get_object_or_404(Formulario, pk=pk, operador=request.user)
    if request.method == 'POST':
        form = FormularioForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('listar_registros')
    else:
        form = FormularioForm(instance=registro)
    return render(request, 'modificar_registro.html', {'form': form})