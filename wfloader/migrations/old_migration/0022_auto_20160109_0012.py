# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0021_auto_20160108_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trade_type', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='trade',
            name='description',
        ),
        migrations.AddField(
            model_name='trade',
            name='trade_type',
            field=models.ForeignKey(default='none exist', blank=True, to='wfloader.Trade_Type'),
            preserve_default=False,
        ),
    ]
