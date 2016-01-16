# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0008_auto_20160106_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='more_info',
            field=models.TextField(null=True, blank=True),
        ),
    ]
