from django.urls import path
from apps.ventas.views import index

urlpatterns = [
    path ('',index, name='index'),
]
