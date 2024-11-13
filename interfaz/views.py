from django.shortcuts import render
from django.http import HttpResponse
from .models import usuarios
from .forms import FormUsuarios

#importamos librerias para login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages



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

def validar_usuarios_login(request):
    if request.method == 'POST':
        try:
            datos_usuario = usuarios.objects.get(usuario=request.POST['usuario'],
                                                  clave=request.POST['clave'])
            request.session['usuario'] = datos_usuario.usuario
            request.session['clave'] = datos_usuario.clave
            messages.success(request, 'Bienvenidos al Sistema de Tickets de Tren')

            return render(request, 'interfaz/inicio.html',{
            'sistema':"Sistema de Tickets RW",
            'materia': "Programacion Web",
            })
        except usuarios.DoesNotExist as e:
            messages.error(request, "Existe un error en los datos, verificalo con el administrador")
    return render(request,'interfaz/login.html')

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

