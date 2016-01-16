# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0021_auto_20160109_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='ticker',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='wkn',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='investor',
            name='desc',
            field=models.TextField(default='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='investor',
            name='got_meta',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='price',
            name='asset',
            field=models.ForeignKey(default='', blank=True, to='wfloader.Asset'),
        ),
        migrations.AlterField(
            model_name='price',
            name='date',
            field=models.DateTimeField(default='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.FloatField(default='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='got_comments',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='got_meta',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='got_price',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='got_trades',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='investable',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='maybe_lerveraged',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='real_money_pf',
            field=models.BooleanField(default=False),
        ),
    ]
