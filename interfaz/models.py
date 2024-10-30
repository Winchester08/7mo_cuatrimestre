from django.db import models

class usuarios(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre Usuario', default='Nombre x')
    usuario = models.CharField(max_length=30, verbose_name='Usuario')
    clave = models.CharField(max_length=10, verbose_name='Clave')
    tipo_usuario=models.CharField(max_length=20, verbose_name='Tipo Usuario')
    verificacion = models.CharField(max_length=2, verbose_name='Verificacion', default='1')


