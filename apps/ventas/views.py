import json
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from apps.ventas.forms import ProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.ventas.models import Producto
from apps.ventas.serializers import ProductoSerializer


# Create your views here.

def lista(request):
    lista = serializers.serialize('json', Producto.objects.all())
    return HttpResponse(lista, content_type='application/json')



def index(request): #formulario def en funcion
    return render (request, 'venta/index.html') 


class ProductoList(ListView):
    model = Producto
    template_name = 'venta/venta_list.html'  

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'venta/venta_form.html'
    success_url = reverse_lazy('venta_listar')    

class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'venta/venta_form.html'
    success_url = reverse_lazy('venta_listar')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'venta/venta_delete.html'
    success_url = reverse_lazy('venta_listar')



class ProductoAPi(APIView):
    serializer = ProductoSerializer

    def get(self, request,format=None):
     lista = Producto.objects.all()
     response = self.serializer(lista, many=True)

     return HttpResponse(json.dumps(response.data), content_type='application/json')

