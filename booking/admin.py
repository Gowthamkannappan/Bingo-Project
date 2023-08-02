from django.contrib import admin
from .models import Vehicle, Complaint, Service

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'application']
    list_filter = ['type', 'application']
    search_fields = ['name', 'type', 'application']

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['complaint_type', 'complaint_description']
    list_filter = ['complaint_type']
    search_fields = ['complaint_type', 'complaint_description']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'vehicle', 'component' ,'service_booking_date','mobile', 'service_type']
    list_filter = ['service_type']
    search_fields = ['name', 'vehicle__name', 'component','service_booking_date','mobile']

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Service, ServiceAdmin)
