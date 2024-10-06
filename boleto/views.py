from django.shortcuts import render


def captura(request):
    return render(request, 'boleto/captura.html',{})
