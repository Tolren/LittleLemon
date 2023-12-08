from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('menu/', MenuView.as_view()),
    path('menu/<int:pk>', SingleMenuView.as_view()),
]