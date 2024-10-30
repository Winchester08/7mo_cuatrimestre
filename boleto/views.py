from django.shortcuts import render
from . models import boleto
from . forms import Captura_Form


def captura(request):
    ventana = "Ventana de Captura de Tickets"
    cap_boleto = Captura_Form()
    return render(request, 'boleto/captura.html',{
        'msj':ventana,
        'fecha':cap_boleto
    })

def listado(request):
    ventana = "Boletos actualmente"
    return render(request, 'boleto/listado_datos.html')