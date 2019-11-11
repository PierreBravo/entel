from django.urls import path
from apps.vendedor.views import index_vendedor


urlpatterns = [
    path ('',index_vendedor),
]
