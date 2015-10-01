from django.db import models


# Create your models here.
class Flow(models.Model):
    datetime_started = models.DateTimeField(help_text='''The datetime that the
                                                       flow was first seen.''')
    # https://docs.python.org/3/library/decimal.html#module-decimal
    # https://docs.python.org/3/library/datetime.html#datetime.timedelta
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#durationfield
    duration = models.DurationField(help_text='''Duration of the flow in
                                                 seconds.''')
    # https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.GenericIPAddressField
    source_ip = models.GenericIPAddressField(protocol='both', help_text='''
        Source IP Address of the flow. (IPv4 or IPv6).''')
    destination_ip = models.GenericIPAddressField(protocol='both', help_text='''
        Destination IP Address of the flow. (IPv4 or IPv6).''')
    source_port = models.PositiveIntegerField(help_text='''Source Port Number
        of the flow.''')
    destination_port = models.PositiveIntegerField(help_text='''Destination Port Number
        of the flow.''')
    source_asn = models.CharField(max_length=21, help_text='''AS number of the
        source IP Address.''')
    destination_asn = models.CharField(max_length=21, help_text='''AS number of the
        destination IP Address.''')
    protocol = models.CharField(max_length=8, help_text='''Protocol of the
        flow.''')
    flows = models.PositiveIntegerField(help_text='''Number of flows.''')
    bytes_transferred = models.BigIntegerField(help_text='''Number of bytes
        transferred in this aggregate of flows.''')
    data_source = models.CharField(max_length=30, help_text='''The source
        of the flow data.''')

    def __unicode__(self):
        return u'%s' % self.datetime_started
