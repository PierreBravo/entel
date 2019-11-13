from django.urls import path, re_path 
from apps.vendedor.views import index_vendedor, VendedorList, VendedorCreate, VendedorUpdate, VendedorDelete

urlpatterns = [
  path ('',index_vendedor),
  path ('vendedor/listar',VendedorList.as_view(), name='vendedor_listar'),
  path ('vendedor/nueva',VendedorCreate.as_view(), name='vendedor_crear'),
  re_path (r'^vendedor/editar/(?P<pk>\d+)/$',VendedorUpdate.as_view(), name='vendedor_editar'),
  re_path (r'^vendedor/eliminar/(?P<pk>\d+)/$', VendedorDelete.as_view(), name='vendedor_eliminar'),
]
