# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0014_auto_20160106_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wikifolio',
            name='isin',
        ),
        migrations.RemoveField(
            model_name='wikifolio',
            name='wikifolio_isin',
        ),
    ]

