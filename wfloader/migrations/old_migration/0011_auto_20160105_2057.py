# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0010_auto_20160105_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wikifolio',
            old_name='Wiki_ID',
            new_name='wiki_id',
        ),
    ]
