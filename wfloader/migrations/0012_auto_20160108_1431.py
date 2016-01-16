# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0011_auto_20160106_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='close_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='price',
            name='high_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='price',
            name='low_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='price',
            name='open_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='price',
            name='price_intervall',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wiki_price',
            name='close_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wiki_price',
            name='high_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wiki_price',
            name='low_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wiki_price',
            name='open_price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wiki_price',
            name='price_intervall',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
