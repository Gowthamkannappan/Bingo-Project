from django.contrib import admin
from .models import Vehicle, Complaint, Service

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'application']
    list_filter = ['type', 'application']
    search_fields = ['name', 'type', 'application']

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['complaint_type', 'complaint_description', 'email']
    list_filter = ['complaint_type']
    search_fields = ['complaint_type', 'complaint_description', 'email']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'vehicle', 'service_booking_date', 'service_type', 'email']
    list_filter = ['service_type']
    search_fields = ['name', 'vehicle__name', 'service_booking_date', 'email']

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Service, ServiceAdmin)
