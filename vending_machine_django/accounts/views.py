"""
Generate relevant functions to perform CRUD API behaviors
"""
from rest_framework import viewsets

from .forms import ItemSerializer, OrderSerializer, VendingSerializer
from .models import Order, Product, VendingMachine


class VendingAPIView(viewsets.ModelViewSet):
    queryset = VendingMachine.objects.all()
    serializer_class = VendingSerializer


class ItemAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer


class StockAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
