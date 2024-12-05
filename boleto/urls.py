from django.urls import path, include
from . import views

urlpatterns = [
   path('boleto/',views.captura,name='captura_ticket'),
   path('archivo/',views.pdf_file, name='gen_archivo'),
   path('listado_boletos/', views.listado_salidas, name='salidas'),
   path('borrado/<int:id>', views.borrado_boletos, name='eliminar_boleto'),
   path('actualizado/<int:id>', views.actualizacion_boleto, name='actualizar'), 
   path('impresion/', views.imprimir_documento, name='impresion'),
   path('reimpresion/<int:id>', views.new_impresion, name='nueva_impresion'),
   path('hacer_actualizacion/<int:id>', views.cambia_boleto, name='accion_boleto')
]