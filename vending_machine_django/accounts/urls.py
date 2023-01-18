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
    # path('vending/', views.VendingAPIView.as_view()),
    path('', include(router.urls)),
    # path('stock/'),

    # other routing (more fancy)
    path('', views.home, name="home"),
    path('products/', views.product, name="products"),
    path('vending_machine/<str:pk>/', views.vending_machine, name="vending_machine"),
    path('create_vending/', views.createVending, name="create_vending"),
    path('create_product/', views.createProduct, name="create_product"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('edit_order/<str:pk>/', views.editOrder, name="edit_order"),
    path('remove_order/<str:pk>/', views.removeOrder, name="remove_order"),
]
