from django.urls import path, include
from . import views

urlpatterns = [
    path('captura_datos/', views.captura),
]