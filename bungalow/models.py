from django.db import models

# Create your models here.

class Property(models.Model):
    AREA_UNITS = (
        ('SqFt', 'Square Feet'),
    )
    area_unit = models.CharField(max_length=10, choices=AREA_UNITS)
    bathrooms = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    home_size = models.PositiveIntegerField()
    HOME_TYPE = (
        ('SingleFamily', 'Single Family'),
        ('Miscellaneous', 'Miscellaneous'),
        ('VacantResidentialLand', 'Vacant Residential Land'),
        ('MultiFamily2To4', 'Multiple Family 2 to 4'),
        ('Condominium', 'Condominium'),
        ('Duplex', 'Duplex'),
        ('Apartment', 'Apartment'),
    )
    home_type = models.CharField(max_length=60, choices=HOME_TYPE)
    last_sold_date = models.DateField()
    last_sold_price = models.PositiveIntegerField()
    link = models.URLField()
    price = models.CharField(max_length=60)
    property_size = models.PositiveIntegerField()
    rent_price = models.CharField(max_length=60)
    rentzestimate_amount = models.PositiveIntegerField()
    rentzestimate_last_updated = models.DateField()
    tax_value = models.PositiveIntegerField()
    tax_year = models.CharField(max_length=4)
    year_built = models.CharField(max_length=4)
    zestimate_amount = models.PositiveIntegerField()
    zestimate_last_updated = models.DateField()
    zillow_id = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
    