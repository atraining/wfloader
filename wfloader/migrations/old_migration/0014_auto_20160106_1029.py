# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wfloader', '0013_auto_20160106_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_ask',
            new_name='ask',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_aum',
            new_name='aum',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_bid',
            new_name='bid',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='create_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_emission',
            new_name='emission',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_general_fee',
            new_name='general_fee',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_isin',
            new_name='isin',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_longdesc',
            new_name='longdesc',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_manager',
            new_name='manager',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_perf_fee',
            new_name='perf_fee',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_shortdesc',
            new_name='shortdesc',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_universe',
            new_name='universe',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_volume',
            new_name='volume',
        ),
        migrations.RenameField(
            model_name='wikifolio',
            old_name='wikifolio_wkn',
            new_name='wkn',
        ),
    ]
