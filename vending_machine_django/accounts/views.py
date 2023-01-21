from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets


class VendingAPIView(viewsets.ModelViewSet): #APIView
    queryset = Vending_Machine.objects.all()
    serializer_class = VendingSerializer
    # def get(self, request):
    #     allVending = Vending_Machine.objects.all().values()
    #     context = {'allVending': allVending}
    #     return Response(context)
    #
    # def post(self, request):
    #     Vending_Machine.objects.create(
    #         name=request.data['name'],
    #         location=request.data['location'],
    #         date_created=request.data['date_created']
    #     )
    #     allVending = Vending_Machine.objects.all().filter(name=request.data['name']).values()
    #     context = {'allVending': allVending}
    #     return Response(context)
    #
    # def delete(self, request):
    #     return Response()


class ItemAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ItemSerializer

class StockAPIView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def home(request):
    orders = Order.objects.all()
    vending = Vending_Machine.objects.all()
    context = {'orders': orders, 'vending': vending}
    return render(request, 'accounts/dashboard.html', context)


def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def vending_machine(request, pk):
    vending = Vending_Machine.objects.get(id=pk)
    orders = vending.order_set.all()  # grabs all of a particular customer's orders
    order_count = orders.count()
    context = {'vending': vending, 'orders': orders, 'orders_count': order_count}
    return render(request, 'accounts/vending_machine.html', context)


def createProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def createVending(request):
    form = VendingForm()
    if request.method == 'POST':
        form = VendingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def createOrder(request, pk):
    vending = Vending_Machine.objects.get(id=pk)
    form = OrderForm(initial={'vending_machine': vending})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def editOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def removeOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'accounts/remove.html', context)