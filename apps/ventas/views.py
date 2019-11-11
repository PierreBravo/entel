from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): #formulario def en funcion
    return render (request, 'venta/index.html') 