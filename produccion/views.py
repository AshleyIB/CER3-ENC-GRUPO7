from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Produccion, Producto, Planta 
from .forms import ProduccionForm
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import Http404
import requests
from django.conf import settings


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
               
        if request.user.groups.filter(name='operario').exists:
            if form.is_valid():
                produccion = form.save(commit=False)
                produccion.operador = request.user
                produccion.save()
                mensaje = f'{produccion.fecha_produccion} {produccion.hora_registro} {produccion.codigo_combustible.planta.codigo} – Nuevo Registro de Producción – {produccion.codigo_combustible.codigo} {produccion.litros_producidos} lts | Total Almacenado: {produccion.litros_producidos}'
                enviar_notificacion_slack(mensaje)
                return redirect('listado_produccion')
        else:
            form = ProduccionForm()
            return render(request, 'produccion/registro_produccion.html', {'form': form, 'mensaje': 'Usted no es operador'})

    else:
        form = ProduccionForm()
    return render(request, 'produccion/registro_produccion.html', {'form': form})

@login_required
def listado_produccion(request):
    producciones = Produccion.objects.filter(operador=request.user, anulado=False)
    

    if request.user.is_staff:
        producciones = Produccion.objects.filter(anulado=False).select_related('codigo_combustible__planta', 'operador')
    else:
        producciones = Produccion.objects.filter(operador=request.user, anulado=False).select_related('codigo_combustible__planta', 'operador')

    return render(request, 'produccion/listado_produccion.html', {'producciones': producciones})

@login_required
def editar_produccion(request, id):
    #produccion = get_object_or_404(Produccion, id=id, operador=request.user)
    produccion = get_object_or_404(Produccion, id=id)
    if request.method == 'POST':
        form = ProduccionForm(request.POST, instance=produccion)
        if form.is_valid():
            form.modificado_por = request.user
            form.fecha_modificacion = timezone.now()
            form.save()
            return redirect('listado_produccion')
    else:
        form = ProduccionForm(instance=produccion)
    return render(request, 'produccion/editar_produccion.html', {'form': form})

