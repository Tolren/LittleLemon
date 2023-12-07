from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *

def index(request):
    return render(request, 'index.html', {})

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer