# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0022_auto_20160109_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikifolio',
            name='full_html',
            field=models.TextField(null=True, blank=True),
        ),
    ]
