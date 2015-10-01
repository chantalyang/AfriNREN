# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AfriNREN_Vis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='destination_asn',
            field=models.CharField(help_text=b'AS number of the\n        destination IP Address.', max_length=21),
        ),
    ]
