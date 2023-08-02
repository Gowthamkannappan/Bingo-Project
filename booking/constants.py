APPLICATION_CHOICES = (
    ('Agriculture', 'Agriculture'),
    ('Commercial', 'Commercial'),
    ("Domestic", 'Domestic'),
)

COMPLAINT_CHOICES = (
    ('GENERAL_CHECKUP', 'General Checkup'),
    ('SPECIFIC_COMPLAINT', 'Specific Complaint'),
)

SERVICE_CHOICES=(
    ('Single Cyl- Pump', 'Single Cyl- Pump'),
    ('VE - Pump', 'VE - Pump'),
    ('Inline 6cyl - Pump', 'Inline 6cyl - Pump'),
    ('Inline 4cyl - Pump', 'Inline 4cyl - Pump'),
    ('Inline 3cyl - Pump', 'Inline 3cyl - Pump'),
    ('VE-EDC - Pump', 'VE-EDC - Pump'),
    ('CRDI - Pump', 'CRDI - Pump'),
    ('China - Pump', 'China - Pump'),
    ('Injectors only', 'Injectors Only'),
    ('CR-Injectors Only', 'CR-Injectors Only'),

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
