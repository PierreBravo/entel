from django.urls import path, re_path
from django.contrib.auth.decorators import login_required
from apps.ventas.views import lista, index,ProductoCreate, ProductoList, ProductoUpdate,ProductoDelete, ProductoAPi

urlpatterns = [
    path ('',index, name='index'),
    path ('nuevo',login_required(ProductoCreate.as_view()), name='venta_crear'),
    path ('listar',login_required(ProductoList.as_view()), name='venta_listar'),
    re_path (r'^venta/update/(?P<pk>\d+)/$',login_required(ProductoUpdate.as_view()), name='venta_editar'),
    re_path (r'^venta/delete/(?P<pk>\d+)/$',login_required(ProductoDelete.as_view()), name='venta_eliminar'),
    path('listado',lista, name="listado"),
    path('api',ProductoAPi.as_view(), name="api"),



]
