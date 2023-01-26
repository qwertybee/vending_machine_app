from django.forms import ModelForm
from .models import *
from rest_framework import serializers

# FORMS AKA 'SERIALIZERS'

class VendingSerializer(serializers.ModelSerializer): #serializers.Serializer
    class Meta:
        model = Vending_Machine
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class VendingForm(ModelForm):
    class Meta:
        model = Vending_Machine
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
