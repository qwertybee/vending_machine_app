"""
Registered models to sqlite's admin database panel
"""
from django.contrib import admin

# Register your models here.
from .models import Order, Product, VendingMachine

admin.site.register(VendingMachine)
admin.site.register(Product)
admin.site.register(Order)
