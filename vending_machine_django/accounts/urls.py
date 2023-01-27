from django.urls import path
from . import views
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register('vending', views.VendingAPIView, basename='vending')
router.register('item', views.ItemAPIView, basename='item')
router.register('stock', views.StockAPIView, basename='stock')

urlpatterns = [
    # basic APIs
    path('', include(router.urls)),
]
