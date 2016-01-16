# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0012_auto_20160108_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wiki_price',
            old_name='price_intervall',
            new_name='price_interval',
        ),
    ]
