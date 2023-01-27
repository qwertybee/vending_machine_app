from django.db import models


class Vending_Machine(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    vending_machine = models.ForeignKey(Vending_Machine, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name
