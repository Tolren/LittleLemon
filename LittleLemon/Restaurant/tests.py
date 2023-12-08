from django.test import TestCase
from .models import *
from rest_framework import serializers

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)
        
class MenuViewTest(TestCase):
    def setup(self):
        item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item2 = Menu.objects.create(title="cerere", price=80, inventory=100)
    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = serializers.Serializer(items, many=True)
        self.assertEqual(len(items), len(serialized_items.data))