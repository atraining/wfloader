# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0014_auto_20160108_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wiki_price',
            name='price_interval',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
