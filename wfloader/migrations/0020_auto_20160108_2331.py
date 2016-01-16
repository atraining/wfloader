# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0019_auto_20160108_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='asset_count_after_trade',
            new_name='num_asset_after',
        ),
        migrations.RenameField(
            model_name='trade',
            old_name='asset_count_before_trade',
            new_name='num_asset_change',
        ),
    ]
