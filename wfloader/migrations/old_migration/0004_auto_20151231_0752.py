# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0003_wikifolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, null=True, blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='wikifolio',
            name='owner',
            field=models.ForeignKey(to='wfloader.Investor', blank=True),
        ),
    ]
