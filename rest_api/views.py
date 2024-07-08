from rest_framework import generics
from produccion.models import Produccion, Planta, Producto
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .serializers import ProduccionSerializer, ProduccionPorPlantaSerializer, ProduccionFiltradaSerializer
from rest_framework import status




class ProduccionList(generics.ListCreateAPIView):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer

class ProduccionDetail(generics.RetrieveUpdateDestroyAPIView):
    def delete(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer
    

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