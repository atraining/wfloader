# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0016_auto_20160108_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='got_meta',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='got_comments',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='got_meta',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='got_price',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='got_trades',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
