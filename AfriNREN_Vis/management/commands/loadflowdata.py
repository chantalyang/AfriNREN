'''
Load flow data from CSV file to the Postgres DB.

writing django commands:
https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/

loading csv into models:
http://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
http://django-adaptors.readthedocs.org/en/latest/
'''
from django.core.management.base import BaseCommand, CommandError
import csv
# from AfriNREN_Vis.models import Flow


class Command(BaseCommand):
    help = 'Loads flow data into DB'

    def handle(self, *args, **options):
        self.stdout.write('**loading flow data**')
