from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.vendedor.models import Vendedor
from apps.vendedor.forms import VendedorForm

# Create your views here.

def index_vendedor(request): #primera vista
 return HttpResponse("Sola la pagina principal jiji")


class VendedorList(ListView):
    model = Vendedor
    template_name = 'vendedor/vendedor_list.html'

class VendedorCreate(CreateView):
    model = Vendedor
    template_name = 'vendedor/vendedor_form.html'
    form_class = VendedorForm
    success_url = reverse_lazy('vendedor_listar')


    def get_context_data(self, **kwargs):
        context = super(VendedorCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
         context['form'] = self.form_class(self.request.GET)    
        return context

    def post(self, request, *args, **kwargs): # guardar y creacion de la relacion del formulario
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
         vendedor = form.save(commit=True)
         vendedor.save()
         return HttpResponseRedirect(self.get_success_url())
        else:
         return self.render_to_response(self.get_context_data(form=form))    



class VendedorUpdate(UpdateView):
	model = Vendedor
	template_name = 'vendedor/vendedor_form.html'
	form_class = VendedorForm
	success_url = reverse_lazy('vendedor_listar')


	def get_context_data(self, **kwargs):
	    context = super(VendedorUpdate, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    vendedor = self.model.objects.get(id=pk)
	    if 'form' not in context:
	    	context['form'] = self.form_class()
	    context['id'] = pk
	    return context

	

class VendedorDelete(DeleteView):
	model = Vendedor
	template_name = 'Vendedor/vendedor_delete.html'
	success_url = reverse_lazy('vendedor_listar')