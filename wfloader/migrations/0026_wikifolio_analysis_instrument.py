# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0025_auto_20160110_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikifolio',
            name='analysis_instrument',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
