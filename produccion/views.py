from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Produccion, Producto, Planta 
from .forms import ProduccionForm
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import Http404
import requests
from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum


def enviar_notificacion_slack(mensaje):
    url = settings.SLACK_WEBHOOK_URL
    payload = {'text': mensaje}
    headers = {'Content-Type': 'application/json'}
    requests.post(url, json=payload, headers=headers)


@login_required
def index(request):
    return render(request, 'produccion/index.html')




@login_required
def registro_produccion(request):
    if request.method == 'POST':
        form = ProduccionForm(request.POST)
        
        if request.user.groups.filter(name='operario').exists():
            if form.is_valid():
                produccion = form.save(commit=False)
                produccion.operador = request.user
                produccion.save()
                
                total_litros = Produccion.objects.filter(codigo_combustible=produccion.codigo_combustible, anulado=False).aggregate(total_litros=Sum('litros_producidos'))['total_litros']
                
                mensaje = f'{produccion.fecha_produccion} {produccion.hora_registro} {produccion.codigo_combustible.planta.codigo} – Nuevo Registro de Producción – {produccion.codigo_combustible.codigo} {produccion.litros_producidos} lts | Total Almacenado: {total_litros}'
                enviar_notificacion_slack(mensaje)
                request.session['mensaje_exito'] = 'Producción Almacenada'
                return redirect('listado_produccion')
        else:
            return render(request, 'produccion/registro_produccion.html', {'form': form, 'mensaje_error': 'Usted no es operador de planta'})

    else:
        form = ProduccionForm()
    return render(request, 'produccion/registro_produccion.html', {'form': form})

@login_required
def listado_produccion(request):
    mensaje_exito = request.session.get('mensaje_exito', '')
    request.session['mensaje_exito'] = ''
    #producciones = Produccion.objects.filter(operador=request.user, anulado=False)

    if request.user.is_staff:
        # Si el usuario es administrador, obtiene todas las producciones
        producciones = Produccion.objects.filter(anulado=False).select_related('codigo_combustible__planta', 'operador')
    else:
        # Si no es administrador, solo obtiene las producciones del usuario actual
        producciones = Produccion.objects.filter(operador=request.user, anulado=False).select_related('codigo_combustible__planta', 'operador')

    return render(request, 'produccion/listado_produccion.html', {'producciones': producciones, 'mensaje_exito': mensaje_exito})

@login_required
def editar_produccion(request, id):
    #produccion = get_object_or_404(Produccion, id=id, operador=request.user)
    produccion = get_object_or_404(Produccion, id=id)
    
    if request.method == 'POST':
        form = ProduccionForm(request.POST, instance=produccion)
        if form.is_valid():
            produccion = form.save(commit=False)
            produccion.modificado_por = request.user
            produccion.fecha_modificacion = timezone.now()
            produccion.save()
            return redirect('listado_produccion')
    else:
        form = ProduccionForm(instance=produccion)
    return render(request, 'produccion/editar_produccion.html', {'form': form})