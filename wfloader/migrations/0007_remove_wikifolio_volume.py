# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0006_auto_20160106_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wikifolio',
            name='volume',
        ),
    ]
