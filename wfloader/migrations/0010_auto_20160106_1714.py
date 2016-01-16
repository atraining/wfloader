# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0009_investor_more_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='more_info',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
