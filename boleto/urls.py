from django.urls import path, include
from . import views

urlpatterns = [
   path('boleto/',views.captura,name='captura_ticket'),
   path('archivo/',views.pdf_file, name='gen_archivo')
 
]