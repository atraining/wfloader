# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0007_comment_wikifolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wikifolio',
            old_name='name',
            new_name='wikiname',
        ),
    ]
