# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0017_auto_20160108_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investment',
            old_name='quantity',
            new_name='asset_count_before_trade',
        ),
        migrations.RenameField(
            model_name='investment',
            old_name='cash',
            new_name='cash_after_trade',
        ),
        migrations.RemoveField(
            model_name='price',
            name='close_price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='high_price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='low_price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='open_price',
        ),
        migrations.RemoveField(
            model_name='price',
            name='price_intervall',
        ),
        migrations.AddField(
            model_name='investment',
            name='asset_count_after_trade',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='change_cash',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='description',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='trade_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='isin',
            field=models.CharField(unique=True, max_length=255, blank=True),
        ),
    ]
