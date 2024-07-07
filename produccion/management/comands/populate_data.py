from django.core.management.base import BaseCommand
from produccion.models import Planta, Combustible

class Command(BaseCommand):
    help = 'Popula la base de datos con datos iniciales'

    def handle(self, *args, **kwargs):
        plantas = [
            {'codigo': 'PRG', 'nombre': 'Planta de Refinación de Gasolina'},
            {'codigo': 'PRD', 'nombre': 'Planta de Refinación de Diesel'},
            {'codigo': 'PRA', 'nombre': 'Planta de Refinación de Combustibles para Aviación'},
        ]

        combustibles = [
            {'codigo': 'G93', 'nombre': 'Gasolina 93 Octanos', 'planta': 'PRG'},
            {'codigo': 'G95', 'nombre': 'Gasolina 95 Octanos', 'planta': 'PRG'},
            {'codigo': 'G97', 'nombre': 'Gasolina 97 Octanos', 'planta': 'PRG'},
            {'codigo': 'DIE', 'nombre': 'Diesel convencional', 'planta': 'PRD'},
            {'codigo': 'DIP', 'nombre': 'Diesel de alto rendimiento', 'planta': 'PRD'},
            {'codigo': 'JA1', 'nombre': 'Jet A-1', 'planta': 'PRA'},
            {'codigo': 'AVG', 'nombre': 'Av Gas', 'planta': 'PRA'},
        ]

        for planta in plantas:
            Planta.objects.get_or_create(codigo=planta['codigo'], nombre=planta['nombre'])

        for combustible in combustibles:
            planta = Planta.objects.get(codigo=combustible['planta'])
            Combustible.objects.get_or_create(codigo=combustible['codigo'], nombre=combustible['nombre'], planta=planta)
            