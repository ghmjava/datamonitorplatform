# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monManager', '0002_auto_20150710_0801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cronjob',
            name='timezone',
        ),
        migrations.RemoveField(
            model_name='intervaljob',
            name='timezone',
        ),
    ]
