from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
#def miapp(request):
#    return HttpResponse("<br>hello world!</br>")

def index(request):
    return render(request, 'index.html')

def acercade(request):
    return render(request, 'acercade.html')