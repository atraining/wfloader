# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0002_wikifolio_isin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wikifolio',
            name='wiki_wkn',
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='wkn',
            field=models.CharField(unique=True, max_length=200, blank=True),
        ),
    ]
