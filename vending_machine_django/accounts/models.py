from django.db import models


class Vending_Machine(models.Model):  # will be named VendingMachine later
    name = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):  # just description of each product
    name = models.CharField(max_length=20, null=True)
    price = models.PositiveIntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):  # status is Order or what stuff vendingmachine/customer got in there
    vending_machine = models.ForeignKey(Vending_Machine, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    # product = models.CharField(max_length=20, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.product.name
