# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0012_wikifolio_wikifolio_longdesc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wikifolio',
            old_name='begin',
            new_name='create_date',
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_ask',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_aum',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_bid',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_emission',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_general_fee',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_isin',
            field=models.CharField(default='refill by model change', unique=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_manager',
            field=models.CharField(default='refill by model change', unique=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_perf_fee',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_shortdesc',
            field=models.TextField(default='refill by model change'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_universe',
            field=models.TextField(default='refill by model change'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_volume',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_wkn',
            field=models.CharField(default='refill by model change', unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
