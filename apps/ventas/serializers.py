from rest_framework.serializers import ModelSerializer
from apps.ventas.models import Producto

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre','cantidad','fecha_venta','hora_venta','comentario')