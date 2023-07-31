APPLICATION_CHOICES = (
    ('Agriculture', 'Agriculture'),
    ('Commercial', 'Commercial'),
    ("Domestic", 'Domestic'),
)

COMPLAINT_CHOICES = (
    ('GENERAL_CHECKUP', 'General Checkup'),
    ('SPECIFIC_COMPLAINT', 'Specific Complaint'),
)

VEHICLE_CHOICES = (
    ("Oil Engines", 'Oil Engine'),
    ('Auto', 'Auto'),
    ('Bus', 'Bus'),
    ('Car', 'Car'),
    ('JCB Loader', 'JCB Loader'),
    ('Generator', 'Generator'),
    ('Marine Engines', 'Marine Engines'),
    ('Tractor', 'Tractor'),
    ('Tipper', 'Tipper'),
    ('6 wheel - Truck', '6 wheel - Truck'),
    ('10 wheel - Truck', '10 wheel - Truck'),
    ('12 wheel - Truck', '12 wheel - Truck'),
    ('Tanker Lorry', 'Tanker Lorry'),
    ('Van', 'Van'),
    ('Others', 'Others')
    # Add other choices here
)

QUICK_SERVICE = 'Quick Service'
REGULAR_SERVICE = 'Regular Service'
SERVICE_TYPE_CHOICES = (
    (QUICK_SERVICE, 'Quick Service'),
    (REGULAR_SERVICE, 'Regular Service'),
)
