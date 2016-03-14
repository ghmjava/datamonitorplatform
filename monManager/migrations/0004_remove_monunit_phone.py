# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monManager', '0003_auto_20150710_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monunit',
            name='phone',
        ),
    ]
