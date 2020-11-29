from rest_framework import viewsets
from .models import Producto
from .serializer import ProductosSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset= Producto.objects.all()
    serializer_class=ProductosSerializer