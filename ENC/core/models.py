from django.db import models


TIPO_USUARIO = (
    ("EPRG","EPRG"),
    ("PRD","PRD"),
    ("PRA","PRA")
)

class Usuario(models.Model):
    codigo= models.CharField(max_length=7)
    contrasena= models.CharField(max_length=10)
    tipo_usuario = models.CharField(max_length=10,choices=TIPO_USUARIO,default="PRD")
    def __str__(self):
        return self.codigo
    
class Formulario(models.Model):
    codigo= models.CharField(max_length=78)
    litros = models.CharField(max_length=200)
    fecha = models.CharField(max_length=100)
    turno = models.CharField(max_length=300)
    hora = models.CharField(max_length=100)
    operador= models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.codigo + self.litros + self.fecha + self.turno + self.hora + self.operador