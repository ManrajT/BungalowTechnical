from django.db import models

# Create your models here.

class Property(models.Model):
    AREA_UNITS = (
        ('SqFt', 'Square Feet'),
    )
    area_unit = models.CharField(max_length=10, choices=AREA_UNITS)
    bathrooms = models.DecimalField(decimal_places=3, max_digits=10, blank=True, null=True)
    bedrooms = models.PositiveIntegerField()
    home_size = models.PositiveIntegerField(blank=True, null=True)
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
    last_sold_date = models.DateField(blank=True, null=True)
    last_sold_price = models.PositiveIntegerField(blank=True, null=True)
    link = models.URLField()
    price = models.CharField(max_length=60)
    property_size = models.PositiveIntegerField(blank=True, null=True)
    rent_price = models.CharField(max_length=60, blank=True, null=True)
    rentzestimate_amount = models.PositiveIntegerField(blank=True, null=True)
    rentzestimate_last_updated = models.DateField(blank=True)
    tax_value = models.DecimalField(decimal_places=2, max_digits=20)
    tax_year = models.CharField(max_length=4)
    year_built = models.CharField(max_length=4, blank=True)
    zestimate_amount = models.PositiveIntegerField(blank=True, null=True)
    zestimate_last_updated = models.DateField()
    zillow_id = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)
