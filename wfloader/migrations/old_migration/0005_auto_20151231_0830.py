# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0004_auto_20151231_0752'),
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
        migrations.AddField(
            model_name='wikifolio',
            name='Wiki_ID',
            field=models.CharField(default=1, unique=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='investable',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='investment',
            name='wikifolio',
            field=models.ForeignKey(to='wfloader.Wikifolio', blank=True),
        ),
    ]
