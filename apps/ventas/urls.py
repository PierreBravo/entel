from django.urls import path, re_path
from apps.ventas.views import index, ProductoCreate, ProductoList, ProductoUpdate,ProductoDelete

urlpatterns = [
    path ('',index, name='index'),
    path ('nuevo',ProductoCreate.as_view(), name='venta_crear'),
    path ('listar',ProductoList.as_view(), name='venta_listar'),
    re_path (r'^venta/update/(?P<pk>\d+)/$',ProductoUpdate.as_view(), name='venta_editar'),
    re_path (r'^venta/delete/(?P<pk>\d+)/$',ProductoDelete.as_view(), name='venta_eliminar'),
]
