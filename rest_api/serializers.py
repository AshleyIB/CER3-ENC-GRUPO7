from rest_framework import serializers
from produccion.models import Produccion, Producto, Planta


class ProduccionSerializer(serializers.ModelSerializer):
    planta_codigo = serializers.CharField(source='codigo_combustible.planta.codigo', read_only=True)
    planta_nombre = serializers.CharField(source='codigo_combustible.planta.nombre', read_only=True)
    combustible_nombre = serializers.CharField(source='codigo_combustible.nombre', read_only=True)
    class Meta:
        model = Produccion
        fields = ['codigo_combustible','planta_codigo','planta_nombre','combustible_nombre','litros_producidos', 'fecha_produccion', 'turno', 'hora_registro', 'operador']

class ProduccionFiltradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produccion
        fields = '__all__'

class ProduccionPorPlantaSerializer(serializers.ModelSerializer):
    planta_codigo = serializers.CharField(source='codigo_combustible.planta.codigo', read_only=True)
    planta_nombre = serializers.CharField(source='codigo_combustible.planta.nombre', read_only=True)
    combustible_nombre = serializers.CharField(source='codigo_combustible.nombre', read_only=True)
    total_produccion = serializers.FloatField()

    class Meta:
        model = Produccion
        fields = ['planta_codigo', 'planta_nombre', 'combustible_nombre', 'total_produccion']