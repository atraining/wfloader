# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0013_auto_20160108_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wiki_price',
            name='price',
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='maybe_lerveraged',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='real_money_pf',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='updated_prices_on',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wiki_price',
            name='price_interval',
            field=models.CharField(default='60', unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
