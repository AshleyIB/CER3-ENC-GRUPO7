from rest_framework import generics
from produccion.models import Produccion, Planta, Producto
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .serializers import ProduccionPorPlantaSerializer, ProduccionFiltradaSerializer
from rest_framework import status


class ProduccionFiltradaView(generics.ListAPIView):
    serializer_class = ProduccionFiltradaSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year', None)
        month = self.request.query_params.get('month', None)

        queryset = Produccion.objects.filter(
            fecha_produccion__year=year,
            fecha_produccion__month=month
        )
        return queryset


class ProduccionPorPlantaView(generics.ListAPIView):
    serializer_class = ProduccionPorPlantaSerializer
    
    def get_queryset(self):

        queryset = Produccion.objects.values('codigo_combustible').annotate(
            total_produccion=Sum('litros_producidos')
        )

        return queryset