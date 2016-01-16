# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0011_auto_20160105_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikifolio',
            name='wikifolio_longdesc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
