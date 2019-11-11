from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_vendedor(request): #primera vista
 return HttpResponse("Sola la pagina principal jiji")