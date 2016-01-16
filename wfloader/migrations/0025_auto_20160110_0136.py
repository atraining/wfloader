# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0024_auto_20160110_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetUniverse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('available_to_wikifolio', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='assetcategory',
            name='used_by',
        ),
        migrations.RemoveField(
            model_name='assetcategory',
            name='wikifolio',
        ),
        migrations.AddField(
            model_name='assetuniverse',
            name='asset_category',
            field=models.ForeignKey(to='wfloader.AssetCategory'),
        ),
        migrations.AddField(
            model_name='assetuniverse',
            name='wikifolio',
            field=models.ForeignKey(to='wfloader.Wikifolio'),
        ),
        migrations.AddField(
            model_name='wikifolio',
            name='assetcategory',
            field=models.ManyToManyField(to='wfloader.AssetCategory', through='wfloader.AssetUniverse'),
        ),
    ]
