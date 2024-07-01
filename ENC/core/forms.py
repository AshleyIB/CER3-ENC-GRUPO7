from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['codigo', 'litros', 'fecha', 'turno', 'hora', 'operador']