from django.urls import path
from apps.usuario.views import RegistroUsuario


urlpatterns = [
    path ('registrar',RegistroUsuario.as_view(), name='registrar'),
]