# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('content', models.TextField()),
                ('asset', models.ForeignKey(to='wfloader.Asset', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.FloatField(null=True, blank=True)),
                ('cash', models.FloatField(null=True, blank=True)),
                ('asset', models.ForeignKey(to='wfloader.Asset', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wiki_Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wikifolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('wiki_id', models.CharField(unique=True, max_length=200)),
                ('wkn', models.CharField(unique=True, max_length=200, blank=True)),
                ('manager', models.CharField(max_length=200, blank=True)),
                ('shortdesc', models.TextField(null=True, blank=True)),
                ('longdesc', models.TextField(null=True, blank=True)),
                ('universe', models.TextField(null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('bid', models.FloatField(null=True, blank=True)),
                ('ask', models.FloatField(null=True, blank=True)),
                ('aum', models.FloatField(null=True, blank=True)),
                ('emission', models.FloatField(null=True, blank=True)),
                ('general_fee', models.FloatField(null=True, blank=True)),
                ('perf_fee', models.FloatField(null=True, blank=True)),
                ('volume', models.FloatField(null=True, blank=True)),
                ('investable', models.BooleanField()),
                ('wikiname', models.CharField(max_length=255, null=True, blank=True)),
                ('end', models.DateTimeField(null=True, blank=True)),
                ('owner', models.ForeignKey(blank=True, to='wfloader.Investor', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wiki_price',
            name='wikifolio',
            field=models.ForeignKey(to='wfloader.Wikifolio', blank=True),
        ),
        migrations.AddField(
            model_name='investment',
            name='wikifolio',
            field=models.ForeignKey(to='wfloader.Wikifolio', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='wikifolio',
            field=models.ForeignKey(to='wfloader.Wikifolio', blank=True),
        ),
    ]
