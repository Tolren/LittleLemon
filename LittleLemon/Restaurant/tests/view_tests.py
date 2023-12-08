from django.test import TestCase
from Restaurant.models import *
from rest_framework import serializers

class MenuViewTest(TestCase):
    def setup(self):
        item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        item2 = Menu.objects.create(title="cerere", price=80, inventory=100)
    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = serializers.Serializer(items, many=True)
        self.assertEqual(len(items), len(serialized_items.data))