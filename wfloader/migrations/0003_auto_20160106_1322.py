# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0002_auto_20160106_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikifolio',
            name='isin',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='manager',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='wkn',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
