from django.shortcuts import render


def captura(request):
    ventana = "Ventana de Captura de Tickets"
    return render(request, 'boleto/captura.html',{
        'msj':ventana
    })
