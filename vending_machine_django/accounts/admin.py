from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Vending_Machine)
admin.site.register(Product)
admin.site.register(Order)