# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0003_auto_20160106_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wikifolio',
            name='manager',
        ),
        migrations.AddField(
            model_name='investor',
            name='nick_name',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
