# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0018_auto_20160108_2306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trade_date', models.DateTimeField(null=True, blank=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('asset_count_before_trade', models.FloatField(null=True, blank=True)),
                ('asset_count_after_trade', models.FloatField(null=True, blank=True)),
                ('change_cash', models.FloatField(null=True, blank=True)),
                ('cash_after_trade', models.FloatField(null=True, blank=True)),
                ('asset', models.ForeignKey(to='wfloader.Asset', blank=True)),
                ('wikifolio', models.ForeignKey(to='wfloader.Wikifolio', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='investment',
            name='asset',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='wikifolio',
        ),
        migrations.DeleteModel(
            name='Investment',
        ),
    ]
