from django.db import models

# Function to validate the postal code 

def validate_postal_code(value):
    if not value.isdigit() or len(value) != 6:
        raise models.ValidationError("Postal code must be a 6-digit number.")

COMPONENT_CHOICES=(
    ("Diesel-Pump","Diesel-Pump"),
    ("Crdi","Crdi"),
    ('Injectors',"Injectors"),
    ("Starter-Motor","Starter-Motor"),
    ('Alternator','Alternator')   
)