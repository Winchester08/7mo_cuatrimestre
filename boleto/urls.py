from django.urls import path, include
from . import views

urlpatterns = [
   path('captura/',views.captura,name='captura')
]