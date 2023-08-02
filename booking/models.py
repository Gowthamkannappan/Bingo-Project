from django.db import models
from .constants import *                             #Choices for all models
from cloudinary.models import CloudinaryField        #to upload image to CDN


class Vehicle(models.Model):                         #To Select vehicle Name and Vehicle type and application
    name = models.CharField(
        'Vehicle Name',
        max_length=100
        )
    type = models.CharField(
        "Vehicle Type",
        max_length=50,
        choices=VEHICLE_CHOICES
        )
    application = models.CharField(
        'Vehicle Application',
        max_length=255,
        choices=APPLICATION_CHOICES
    )

    def __str__(self):
        return self.name

class Complaint(models.Model):                      # To select Nature of Complaint and Description and Image and video
    complaint_type = models.CharField(
        max_length=250, 
        choices=COMPLAINT_CHOICES
    )
    complaint_description = models.CharField(
        'Complaint Description',
        max_length=500,
        blank=True,
        null=True
    )
    complaint_image_1 = CloudinaryField(
        'Complaint Image 1',
        blank=True,
        null=True
    )
    complaint_image_2 = CloudinaryField(
        'Complaint Image 2', 
        blank=True,
        null=True
    )
    complaint_image_3 = CloudinaryField(
        'Complaint Image 3', 
        blank=True, 
        null=True
    )
    complaint_video = CloudinaryField(
        'Complaint Video',
        blank=True, 
        null=True, 
        resource_type='video'
    )
    def __str__(self):
        return f"{self.complaint_type} - {self.complaint_description}" 

class Service(models.Model):                        #to Avail what type of service and Book

    vehicle = models.ForeignKey(
        Vehicle, 
        on_delete=models.CASCADE
    )
    complaint = models.ManyToManyField(
        'Complaint',
        blank=True
    )
    component=models.CharField(
        "Component",
        max_length=75,
        choices=SERVICE_CHOICES
        )
    name = models.CharField(
        'Customer Name',
        max_length=100
    )
    mobile = models.IntegerField(
        'Mobile',
        blank=False,
    )
    alternate_mobile = models.IntegerField(
        'Alternate Mobile',
        blank=True,
    )
    email = models.EmailField(
        'Email',
        blank=True,
        null=True
    )

    service_booking_date = models.DateField(
        "Booking Date",db_index=True
    )
    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_TYPE_CHOICES
    )
    

    def __str__(self):
        return self.name