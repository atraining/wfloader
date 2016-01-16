# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0007_remove_wikifolio_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='investor',
            name='desc',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='risk_five',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='risk_four',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='risk_one',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='risk_three',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='investor',
            name='risk_two',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
