from django.shortcuts import render
from django.http import HttpResponse

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
