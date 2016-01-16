# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikifolio',
            name='isin',
            field=models.CharField(default=123, unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
