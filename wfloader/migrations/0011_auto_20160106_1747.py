# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0010_auto_20160106_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='date_time',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_id',
            field=models.CharField(default='kk', unique=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='asset',
            field=models.ForeignKey(blank=True, to='wfloader.Asset', null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='wikifolio',
            field=models.ForeignKey(blank=True, to='wfloader.Wikifolio', null=True),
        ),
    ]
