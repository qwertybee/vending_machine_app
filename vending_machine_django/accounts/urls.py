"""
Construct urls via router and ModelViewSet
"""
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("vending", views.VendingAPIView, basename="vending")
router.register("item", views.ItemAPIView, basename="item")
router.register("stock", views.StockAPIView, basename="stock")

urlpatterns = [
    # basic APIs
    path("", include(router.urls)),
]
