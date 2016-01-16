# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0015_auto_20160108_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiki_price',
            name='price_interval',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
