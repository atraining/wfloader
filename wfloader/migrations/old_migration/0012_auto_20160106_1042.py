# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0011_auto_20160105_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wikifolio',
            old_name='begin',
            new_name='created',
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='ask',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='aum',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='bid',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='emission',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='general_fee',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='longdesc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='manager',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='perf_fee',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='shortdesc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='universe',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='volume',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wkn',
            field=models.CharField(unique=True, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='owner',
            field=models.ForeignKey(blank=True, to='wfloader.Investor', null=True),
        ),
    ]
