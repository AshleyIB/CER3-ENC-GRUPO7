from rest_framework import serializers
from produccion.models import Produccion

class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = ['codigo_combustible', 'litros_producidos', 'fecha_produccion', 'turno', 'hora_registro', 'operador']
