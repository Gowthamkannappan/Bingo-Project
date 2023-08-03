from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'mobile_number', 'city', 'component','booking_date', 'created_at']
    search_fields = ['name', 'mobile_number','component', 'city']
    list_filter = ['component', 'booking_date','city']
    # Add any other configuration options you want for the admin interface

# Register the Booking model with the custom admin class
admin.site.register(Booking, BookingAdmin)
