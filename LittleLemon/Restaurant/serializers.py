from rest_framework.serializers import Serializer
from .models import *

class BookingSerializer(Serializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class MenuSerializer(Serializer):
    class Meta:
        model = Menu
        fields = '__all__'