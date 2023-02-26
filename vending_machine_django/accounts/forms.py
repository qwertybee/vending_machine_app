"""
Create forms/serializers for our models.
"""
from rest_framework import serializers

from .models import Order, Product, VendingMachine


class VendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendingMachine
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
