from django.urls import path
from .views import BookingAdd,BookingList

urlpatterns = [
    path('dc', BookingList.as_view(), name='Booking_list'),
    path('addbook', BookingAdd.as_view(), name='Booking_add'),
]
