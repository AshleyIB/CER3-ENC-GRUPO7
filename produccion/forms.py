from django import forms
from .models import Produccion

class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ['codigo_combustible', 'litros_producidos', 'fecha_produccion', 'turno']
