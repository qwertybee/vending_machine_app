from .forms import *
from rest_framework import viewsets


class VendingAPIView(viewsets.ModelViewSet):
    queryset = VendingMachine.objects.all()
    serializer_class = VendingSerializer


class ItemAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer


class StockAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
