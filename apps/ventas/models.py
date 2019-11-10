from django.db import models
from apps.vendedor.models import Vendedor

# Create your models here.

class Venta(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
     return '{}'.format(self.nombre)





class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.FloatField(blank=True, null=True)
    fecha_venta = models.DateTimeField(auto_now_add=True, blank=True)
    comentario = models.TextField() 
    vendedor = models.ForeignKey(Vendedor, null=True, blank=True, on_delete=models.CASCADE)
    venta = models.ManyToManyField(Venta,blank=True)

