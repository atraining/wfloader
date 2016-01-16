# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0020_auto_20160108_2331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='change_cash',
            new_name='cash_change',
        ),
    ]
