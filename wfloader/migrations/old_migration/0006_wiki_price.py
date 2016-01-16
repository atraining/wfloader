# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0005_auto_20151231_0830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki_Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('wikifolio', models.ForeignKey(to='wfloader.Wikifolio', blank=True)),
            ],
        ),
    ]
