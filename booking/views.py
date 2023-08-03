from django.shortcuts import render
from .models import Booking
from rest_framework import generics
from .serializers import BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend



class BookingList(generics.ListAPIView):   # ListAPIView Handles the get method 
    queryset = Booking.objects.order_by('-booking_date').all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['item_id']


class BookingAdd(generics.CreateAPIView):     #CreateAPIView handles the post method.
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer