from .models import Booking
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    complaint_image = serializers.ImageField(write_only = True)
    class Meta:
        model = Booking
        fields = '__all__'