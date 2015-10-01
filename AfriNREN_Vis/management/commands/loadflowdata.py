'''
Load flow data from CSV file to the Postgres DB.

writing django commands:
https://docs.djangoproject.com/en/1.8/howto/custom-management-commands/

loading csv into models:
http://stackoverflow.com/questions/2459979/how-to-import-csv-data-into-django-models
http://django-adaptors.readthedocs.org/en/latest/
'''
from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime, parse_duration
import csv
from AfriNREN_Vis.models import Flow
from datetime import datetime, timedelta
import sys
# from AfriNREN_Vis.models import Flow


class Command(BaseCommand):
    help = 'Loads flow data into DB'

    def handle(self, *args, **options):
        filename = 'newdata.csv'
        csvfilepath = '/Users/rob/dev/AfriNREN-NetFLOW-Scripts/%s' % filename
        self.stdout.write('**loading flow data**')
        with open(csvfilepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_flow = Flow()
                # https://docs.python.org/2/library/datetime.html#datetime.datetime.strptime
                new_flow.datetime_started = parse_datetime(row['Date first seen'])
                new_flow.duration = timedelta(seconds=float(row['Duration']))
                new_flow.source_ip = row['Src IP Addr']
                new_flow.destination_ip = row['Dst IP Addr']
                new_flow.source_port = int(row['Src Pt'])
                new_flow.destination_port = int(float(row['Dst Pt']))
                new_flow.source_asn = row['src_ASN']
                new_flow.destination_asn = row['dst_ASN']
                new_flow.protocol = row['Proto']
                new_flow.flows = int(row['Flows'])
                new_flow.bytes_transferred = int(row['Bytes'])
                new_flow.data_source = filename

                try:
                    new_flow.save()
                except:
                    print "Unexpected Error: ", sys.exc_info()[0]
                    raise
# '''Date first seen,Duration,Src IP Addr,Src Pt,
                # Dst IP Addr,Dst Pt,
                # Proto,Flows,Bytes,src_ASN,
                # dst_ASN'''
