from django.shortcuts import render

from django.http import HttpResponse

from .models import Cliente, Orden
# Create your views here.
# def miapp(request):
#  return HttpResponse("<br>hello world!</br>")

def index(request):
    return render(request, 'index.html')

def acercade(request):
    return render(request, 'acercade.html')

##
def lista_clientes(request):
    clientes = Cliente.objects.all() #obtener registros cliente
    return render(request, 'clientes.html',{'clientes': clientes})

def lista_ordenes(request):
    ordenes = Orden.objects.all() #obtener registros orden
    return render(request, 'ordenes.html',{'ordenes': ordenes}) 
