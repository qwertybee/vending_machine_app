"""
Test units for our models
"""
from django.test import TestCase

from ..models import Product, VendingMachine


class TestVendingMachineModels(TestCase):
    def setUp(self) -> None:
        vm = VendingMachine(
            name="vtest",
            location="location test",
        )
        vm.save()

    def test_vm_created(self) -> None:
        vm = VendingMachine.objects.get(name="vtest")
        self.assertEqual(vm.name, "vtest")
        self.assertEqual(vm.location, "location test")


class TestProductModels(TestCase):
    def setUp(self) -> None:
        product = Product(
            name="xproduct",
            price=999,
        )
        product.save()

    def test_product_created(self) -> None:
        product = Product.objects.get(name="xproduct")
        self.assertEqual(product.name, "xproduct")
        self.assertEqual(product.price, 999)
