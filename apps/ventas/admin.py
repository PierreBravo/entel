from django.contrib import admin
from apps.ventas.models import Venta, Producto

# Register your models here.
admin.site.register(Venta)
admin.site.register(Producto)
