from django.shortcuts import render
from django.http import HttpResponse
from .models import usuarios
from .forms import FormUsuarios


def inicio(request):
    sistema = 'Sistema de Tickets'
    mensaje = 'Bienvenidos'
    return render(request, 'interfaz/inicio.html',{
    'msj':mensaje,
    'sistema': sistema  
    })

def login(request):
    sistema = "Sistema de Tickets RW"
    materia = "Programacion Web"
    return render(request,'interfaz/login.html',{
        'mensaje':'Bienvenidos ventana de Login de usuarios',
        'nombre_sistema':sistema,
        'materia': materia
    })

def usuarios_captura(request):
    sistema = "Sistema de Tickets RW"
    materia = "Programacion Web"
    formulario = FormUsuarios(request.POST)
    if formulario.is_valid():
        formulario.save()
        return HttpResponse("Datos Guardados con exito")
        

    return render(request, 'interfaz/captura_usuarios.html',{
        'mensaje':'Ventana de Captura de usuarios',
        'nombre_sistema':sistema,
        'materia': materia,
        'campos_formulario':formulario,
        'notificacion':'Datos Guardados correctamente'
    })

