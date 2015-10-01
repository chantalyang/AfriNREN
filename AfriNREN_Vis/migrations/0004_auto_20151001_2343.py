# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AfriNREN_Vis', '0003_as'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='as',
            name='id',
        ),
        migrations.AlterField(
            model_name='as',
            name='ASN',
            field=models.CharField(help_text=b'Identification number for the AS', max_length=21, serialize=False, primary_key=True),
        ),
    ]
