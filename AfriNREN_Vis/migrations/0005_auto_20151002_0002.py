# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AfriNREN_Vis', '0004_auto_20151001_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='as',
            name='Organisation',
            field=models.CharField(help_text=b'Name of the organisation that\n                                    owns the AS', max_length=140),
        ),
    ]
