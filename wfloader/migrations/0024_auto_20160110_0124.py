# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0023_wikifolio_full_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asset_category', models.CharField(max_length=255, blank=True)),
                ('used_by', models.BooleanField(default=False)),
                ('wikifolio', models.ForeignKey(to='wfloader.Wikifolio')),
            ],
        ),
        migrations.AlterField(
            model_name='investor',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
    ]
