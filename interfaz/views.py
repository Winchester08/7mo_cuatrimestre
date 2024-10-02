from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse ("<h2>Tickets de tren RW con inicio</h2>")

def login(request):
    sistema = "Sistema de Tickets RW"
    return render(request,'interfaz/login.html',{
        'mensaje':'Bienvenidos ventana de Login de usuarios',
        'nombre_sistema':sistema
    })