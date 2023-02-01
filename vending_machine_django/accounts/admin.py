from django.contrib import admin

# Register your models here.
from .models import VendingMachine, Product, Order

# registered models to sqlite's admin database panel
admin.site.register(VendingMachine)
admin.site.register(Product)
admin.site.register(Order)
