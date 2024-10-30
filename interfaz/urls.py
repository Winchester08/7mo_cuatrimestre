from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('login/', views.login, name='Login'),
    path('captura_usuarios/', views.usuarios_captura, name='nuevo_usuario')
    
]