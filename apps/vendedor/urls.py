from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.vendedor.views import index_vendedor, VendedorList, VendedorCreate, VendedorUpdate, VendedorDelete

urlpatterns = [
  path ('',index_vendedor),
  path ('vendedor/listar',login_required(VendedorList.as_view()), name='vendedor_listar'),
  path ('vendedor/nueva',login_required(VendedorCreate.as_view()), name='vendedor_crear'),
  re_path (r'^vendedor/editar/(?P<pk>\d+)/$',login_required(VendedorUpdate.as_view()), name='vendedor_editar'),
  re_path (r'^vendedor/eliminar/(?P<pk>\d+)/$', login_required(VendedorDelete.as_view()), name='vendedor_eliminar'),
]
