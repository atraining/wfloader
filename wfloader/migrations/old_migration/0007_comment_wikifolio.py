# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0006_wiki_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='wikifolio',
            field=models.ForeignKey(default=1, blank=True, to='wfloader.Wikifolio'),
            preserve_default=False,
        ),
    ]
