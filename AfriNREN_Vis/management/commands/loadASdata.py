'''
Load AS data from CSV file to the Postgres DB.

writing django commands:
https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/

loading csv into models:
http://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
http://django-adaptors.readthedocs.org/en/latest/
'''
from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime, parse_duration
import csv
from AfriNREN_Vis.models import AS
import sys


class Command(BaseCommand):
    help = 'Loads AS data into DB'

    def handle(self, *args, **options):
        filename = 'AS-details.csv'
        csvfilepath = '/Users/rob/dev/AfriNREN-NetFLOW-Scripts/%s' % filename
        self.stdout.write('**loading AS data**')
        with open(csvfilepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                new_AS = AS()
                new_AS.ASN = row['ASN']
                new_AS.Country = row['Country']
                new_AS.Continent = row['Continent']
                new_AS.Organisation = row['Organisation']

                try:
                    new_AS.save()
                    # print(new_AS)
                except:
                    print "Unexpected Error: ", sys.exc_info()[0]
                    raise
# '''Date first seen,Duration,Src IP Addr,Src Pt,
                # Dst IP Addr,Dst Pt,
                # Proto,Flows,Bytes,src_ASN,
                # dst_ASN'''
