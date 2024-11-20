from django.urls import path, include
from . import views

urlpatterns = [
   path('boleto/',views.captura,name='captura_ticket'),
   path('archivo/',views.pdf_file, name='gen_archivo'),
   path('listado_boletos', views.listado_salidas, name='salidas'),
   path('borrado/<int:id>', views.borrado_boletos, name='eliminar_boleto')
   
 
]