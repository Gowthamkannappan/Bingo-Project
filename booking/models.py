from django.db import models
from django.core.validators import RegexValidator # To Validate Mobile Number
from cloudinary.models import CloudinaryField
from .constants import *    # to import Choices for all datafields
# Create your models here.

# Function to validate the postal code 
def validate_postal_code(value):
    if not value.isdigit() or len(value) != 6:
        raise models.ValidationError("Postal code must be a 6-digit number.")
    
class Booking(models.Model):
    class Meta(object):
        db_table='bookings'
        
    component=models.CharField(
        'Product',
        max_length=75,
        blank=True,
        null=True, 
        choices=COMPONENT_CHOICES
    )
    
    vehicle=models.CharField(
        'Vehicle Type',
        max_length=75,
        blank=True,
        null=True,        
    )
    
    name=models.CharField(
        "Customer Name",
        max_length=255,
        blank=False,
        null=False,
        db_index=True
    )
    
    mobile_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[6-9]\d{9}$',
                message="Enter a valid mobile number.",
                code="invalid_mobile_number",
            )
        ],
        unique=True,
        blank=False,
        null=False,
        db_index=True
    )
    
    address=models.TextField(
        "Address",
        max_length=255,
        help_text="Please enter your address here",
        blank=True,
        null=True
    )
    
    city=models.CharField(
        "City/Town",
        max_length=255,
        blank=False,
        null=False,
    )
    
    state=models.CharField(
        'State',
        max_length=50,
        blank=True,
        null=True,
        default='Tamil Nadu'
    )
    
    pincode = models.CharField(
        "Pincode",
        max_length=6, 
        validators=[validate_postal_code]
    )
    
    remarks=models.TextField(
        "Complaint",
        max_length=595,
        help_text="Please enter your complaint here"
    )
    
    complaint_image=CloudinaryField(
        "Complaint Image",
        blank=True,
        null=True,        
    )
    
    booking_date=models.DateTimeField(
        "Booking Date",
        blank=False,
        null=False
    )
    created_at = models.DateTimeField(
        "Created Time",
        auto_now_add=True
    )
    
    
    
    
    