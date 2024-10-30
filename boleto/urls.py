from django.urls import path, include
from . import views

urlpatterns = [
   path('boleto/',views.captura,name='captura_ticket'),
   path('salidas/',views.listado,name='salidas')
]