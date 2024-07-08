from django.urls import path
from . import views


from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro_produccion, name='registro_produccion'),
    path('listado/', views.listado_produccion, name='listado_produccion'),
    path('editar/<int:id>/', views.editar_produccion, name='editar_produccion'),
]
