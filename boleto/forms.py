from django import forms
from . models import boleto

class Captura_Form(forms.ModelForm):
    class Meta:
        model = boleto
        fields = ['fecha']