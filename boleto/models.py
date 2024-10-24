from django.db import models

class trenes(models.Model):
    tren = models.CharField(max_length=4, verbose_name='tren', default='Tren')
    vagon = models.CharField(max_length=4, verbose_name='Vagon', default='1')
    asiento = models.CharField(max_length=10, verbose_name='Asiento', default='1')

class boleto(models.Model):
    fecha = models.DateField(verbose_name='Fecha')
    nombre = models.CharField(max_length=30, verbose_name='Nombre Usuario')
    telefono = models.CharField(max_length=10, verbose_name='Telefono', default='0000')
    num_boleto = models.CharField(max_length=10, verbose_name='Num Boleto')
    origen = models.CharField(max_length=100, verbose_name='Origen')
    destino = models.CharField(max_length=100, verbose_name='Destino')
    fecha_salida = models.DateField(verbose_name='Fecha Salida')
    fecha_llegada = models.DateField(verbose_name='Fecha Llegada')
    hsalida = models.CharField(max_length=15, verbose_name='Hora salida')
    hllegada = models.CharField(max_length=15, verbose_name='Hora llegada')
    tren = models.CharField(max_length=3, verbose_name='Tren', default='1')
    vagon = models.CharField(max_length=3, verbose_name='Vagon', default='1')
    asiento = models.CharField(max_length=3, verbose_name='asiento', default='1')
    precio = models.CharField(max_length=10, verbose_name='asiento', default='0.00')
    folio = models.CharField(max_length=10, verbose_name='folio', default='0000')
    estatus = models.CharField(max_length=30, verbose_name='Estatus', default='Pendiente')
    observaciones = models.CharField(max_length=150, verbose_name='observaciones', default='None')
    nota =models.CharField(max_length=150, verbose_name='notas', default='None')