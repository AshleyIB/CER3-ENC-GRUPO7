from rest_framework import generics
from produccion.models import Produccion
from .serializers import ProduccionSerializer

class ProduccionList(generics.ListCreateAPIView):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer

class ProduccionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer
