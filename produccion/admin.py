from django.contrib import admin
from .models import Planta, Producto, Produccion

admin.site.register(Planta)
admin.site.register(Producto)
admin.site.register(Produccion)