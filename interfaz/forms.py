from django import forms
from .models import usuarios

class FormUsuarios(forms.ModelForm):
    class Meta:
        model = usuarios
        fields = ['nombre','usuario','clave','tipo_usuario','verificacion']

