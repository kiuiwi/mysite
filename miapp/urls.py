from django.urls import path
from . import views

from .views import lista_clientes

urlpatterns = [
    path('', views.index, name='index'),
    path('acercade/', views.acercade, name='acercade'),
    path('clientes/', lista_clientes, name = 'lista_clientes'),
]