# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime_started', models.DateTimeField(help_text=b'The datetime that the\n                                                       flow was first seen.')),
                ('duration', models.DurationField(help_text=b'Duration of the flow in\n                                                 seconds.')),
                ('source_ip', models.GenericIPAddressField(help_text=b'\n        Source IP Address of the flow. (IPv4 or IPv6).')),
                ('destination_ip', models.GenericIPAddressField(help_text=b'\n        Destination IP Address of the flow. (IPv4 or IPv6).')),
                ('source_port', models.PositiveIntegerField(help_text=b'Source Port Number\n        of the flow.')),
                ('destination_port', models.PositiveIntegerField(help_text=b'Destination Port Number\n        of the flow.')),
                ('source_asn', models.CharField(help_text=b'AS number of the\n        source IP Address.', max_length=21)),
                ('destination_asn', models.CharField(help_text=b'AS number of the\n        destination IP Address.', max_length=8)),
                ('protocol', models.CharField(help_text=b'Protocol of the\n        flow.', max_length=8)),
                ('flows', models.PositiveIntegerField(help_text=b'Number of flows.')),
                ('bytes_transferred', models.BigIntegerField(help_text=b'Number of bytes\n        transferred in this aggregate of flows.')),
                ('data_source', models.CharField(help_text=b'The source\n        of the flow data.', max_length=30)),
            ],
        ),
    ]
