from rest_framework import viewsets
from .models import Categoria, Producto, Cliente, Pedido, DetallePedido
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, PedidoSerializer, DetallePedidoSerializer

# Vista para Categoria usando ModelViewSet
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Vista para Producto usando ModelViewSet
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para Cliente usando ModelViewSet
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# Vista para Pedido usando ModelViewSet
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Vista para DetallePedido usando ModelViewSet
class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer