from django.core.management.base import BaseCommand, CommandError
from argparse import RawTextHelpFormatter 
from bungalow.models import Property
import csv 
import datetime 
from pprint import pprint 

class Command(BaseCommand):
    help = """Given a csv file with information on bungalow, ingest that information into relational database

Example:
$> python3 manage.py ingest /Users/manrajtatla/Desktop/challenge_data.csv"""
    
    def create_parser(self, *args, **kwargs):
        parser = super(Command, self).create_parser(*args, **kwargs)
        parser.formatter_class = RawTextHelpFormatter
        return parser

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path',
                            action='store',
                            help='Path to CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file_path']
        with open(csv_file_path, 'r') as csvfile:
            records = csv.DictReader(csvfile, delimiter=',')
            for record in records:
                try:
                    property = Property(
                        area_unit = record['area_unit'],
                        bathrooms = self.parse_decimal(record['bathrooms']), 
                        bedrooms = self.parse_int(record['bedrooms']), 
                        home_size = self.parse_int(record['home_size']), 
                        home_type = record['home_type'], 
                        last_sold_date = self.parse_date(record['last_sold_date']), 
                        last_sold_price = self.parse_int(record['last_sold_price']), 
                        link = record['link'],
                        price = record['price'], 
                        property_size = self.parse_int(record['property_size']),
                        rent_price = record['rent_price'],
                        rentzestimate_amount = self.parse_int(record['rentzestimate_amount']), 
                        rentzestimate_last_updated = self.parse_date(record['rentzestimate_last_updated']),
                        tax_value = record['tax_value'],
                        tax_year = record['tax_year'],
                        year_built = record['year_built'],
                        zestimate_amount = self.parse_int(record['zestimate_amount']),
                        zestimate_last_updated = self.parse_date(record['zestimate_last_updated']),
                        zillow_id = record['zillow_id'],
                        address = record['address'],
                        city = record['city'],
                        state = record['state'],
                        zipcode = record['zipcode']
                        )
                    property.save()
                except Exception as error:
                    print(error)

    def parse_date(self, date):
        if(date == ''):
            return None
        return datetime.datetime.strptime(date, "%m/%d/%Y").date() 
    
    def parse_int(self, integer):
        if(integer == ''):
            return None
        return int(integer)
    
    def parse_decimal(self, decimal):
        if(decimal == ''):
            return None
        return decimal





         

