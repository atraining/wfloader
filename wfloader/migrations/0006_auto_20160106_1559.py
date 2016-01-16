# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0005_remove_wikifolio_shortdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikifolio',
            name='emission',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
