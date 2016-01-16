# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0020_auto_20160108_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade_Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trade_type', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='trade',
            old_name='change_cash',
            new_name='cash_change',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='description',
        ),
        migrations.AddField(
            model_name='trade',
            name='trade_type',
            field=models.ForeignKey(default=1, blank=True, to='wfloader.Trade_Type'),
            preserve_default=False,
        ),
    ]
