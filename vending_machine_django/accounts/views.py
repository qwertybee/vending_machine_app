from .forms import VendingSerializer, ItemSerializer, OrderSerializer
from .models import VendingMachine, Product, Order
from rest_framework import viewsets


# generate relevant functions to perform CRUD API behaviors
class VendingAPIView(viewsets.ModelViewSet):
    queryset = VendingMachine.objects.all()
    serializer_class = VendingSerializer


class ItemAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer


class StockAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
