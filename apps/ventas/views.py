from django.shortcuts import render
from django.http import HttpResponse
from apps.ventas.forms import ProductoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.ventas.models import Producto
# Create your views here.

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
