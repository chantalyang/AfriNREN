# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AfriNREN_Vis', '0002_auto_20150929_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='AS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ASN', models.CharField(help_text=b'Identification number for the AS', max_length=21)),
                ('Country', models.CharField(help_text=b'Country of the AS', max_length=30)),
                ('Continent', models.CharField(help_text=b'Continent of the AS', max_length=20)),
                ('Organisation', models.CharField(help_text=b'Name of the organisation that\n                                    owns the AS', max_length=80)),
            ],
        ),
    ]
