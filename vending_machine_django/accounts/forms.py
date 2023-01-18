from django.forms import ModelForm
from .models import *


# FORMS AKA 'SERIALIZERS'

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
