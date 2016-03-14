# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monunit',
            name='email',
            field=models.TextField(default=b'siweixu@meilishuo.com', verbose_name='\u62a5\u9519\u901a\u77e5\u90ae\u7bb1\u5730\u5740\uff0c\u4ee5\u9017\u53f7\u5206\u9694'),
        ),
        migrations.AddField(
            model_name='monunit',
            name='phone',
            field=models.TextField(default=b'18610274957', verbose_name='\u62a5\u9519\u901a\u77e5\u624b\u673a\uff0c\u4ee5\u9017\u53f7\u5206\u9694'),
        ),
    ]
