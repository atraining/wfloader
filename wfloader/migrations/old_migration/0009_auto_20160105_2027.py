# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0008_auto_20160105_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikifolio',
            name='owner',
            field=models.ForeignKey(to='wfloader.Investor'),
        ),
    ]
