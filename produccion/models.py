from django.db import models
from django.contrib.auth.models import User


class Planta(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Produccion(models.Model):
    codigo_combustible = models.ForeignKey(Producto, on_delete=models.CASCADE)
    litros_producidos = models.FloatField()
    fecha_produccion = models.DateField()
    turno = models.CharField(max_length=2, choices=[('AM', 'Mañana'), ('PM', 'Tarde'), ('MM', 'Noche')])
    hora_registro = models.TimeField(auto_now_add=True)
    operador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='producciones_registradas')
    modificado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='producciones_modificadas')
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    anulado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.codigo_combustible.planta.codigo} - {self.codigo_combustible.codigo} - {self.codigo_combustible.nombre} - {self.fecha_produccion} - {self.turno} - {self.litros_producidos} - {self.operador.first_name} - {self.operador.last_name}'