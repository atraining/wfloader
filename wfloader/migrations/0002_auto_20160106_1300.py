# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikifolio',
            name='isin',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='wkn',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
