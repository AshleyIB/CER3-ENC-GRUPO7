from django.urls import path
from . import views

urlpatterns = [
    path('total-produccion-por-planta/', views.ProduccionPorPlantaView.as_view(), name='produccion-por-planta'),
    path('produccion-filtrada/', views.ProduccionFiltradaView.as_view(), name='produccion-filtrada'),
]