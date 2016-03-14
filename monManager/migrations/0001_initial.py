# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CronJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=None, verbose_name='\u5e74(4\u4f4d\u6570\u5b57)')),
                ('month', models.IntegerField(default=None, verbose_name='\u6708', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('day', models.IntegerField(default=None, verbose_name='\u65e5', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)])),
                ('week', models.IntegerField(default=None, verbose_name='\u5468', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53)])),
                ('day_of_week', models.CharField(default=None, max_length=20, verbose_name='\u4e00\u5468\u4e2d\u7684\u54ea\u5929', choices=[('mon', '\u5468\u4e00'), ('tue', '\u5468\u4e8c'), ('wed', '\u5468\u4e09'), ('thu', '\u5468\u56db'), ('fri', '\u5468\u4e94'), ('sat', '\u5468\u516d'), ('sun', '\u5468\u65e5')])),
                ('hour', models.IntegerField(default=None, verbose_name='\u5c0f\u65f6', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23)])),
                ('minute', models.IntegerField(default=None, verbose_name='\u5206\u949f', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59)])),
                ('second', models.IntegerField(default=None, verbose_name='\u79d2', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59)])),
                ('start_date', models.DateTimeField(default=None, verbose_name='\u4efb\u52a1\u542f\u52a8\u65f6\u95f4')),
                ('end_date', models.DateTimeField(default=None, verbose_name='\u4efb\u52a1\u6301\u7eed\u5230\u5565\u65f6\u7ed3\u675f')),
                ('timezone', models.CharField(default=None, max_length=200, verbose_name='\u65f6\u533a')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='IntervalJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weeks', models.IntegerField(default=0, verbose_name='\u95f4\u9694\u591a\u5c11\u5468')),
                ('days', models.IntegerField(default=0, verbose_name='\u95f4\u9694\u591a\u5c11\u5929')),
                ('hours', models.IntegerField(default=0, verbose_name='\u95f4\u9694\u591a\u5c11\u5c0f\u65f6')),
                ('minutes', models.IntegerField(default=0, verbose_name='\u95f4\u9694\u591a\u5c11\u5206\u949f')),
                ('seconds', models.IntegerField(default=0, verbose_name='\u95f4\u9694\u591a\u5c11\u79d2')),
                ('start_date', models.DateTimeField(default=None, verbose_name='\u4efb\u52a1\u542f\u52a8\u65f6\u95f4')),
                ('end_date', models.DateTimeField(default=None, verbose_name='\u4efb\u52a1\u6301\u7eed\u5230\u5565\u65f6\u7ed3\u675f')),
                ('timezone', models.CharField(default=None, max_length=200, verbose_name='\u65f6\u533a')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='MonUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('funcName', models.CharField(unique=True, max_length=200, verbose_name='\u51fd\u6570\u540d')),
                ('funcBody', models.TextField(verbose_name='\u51fd\u6570\u4e3b\u4f53')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('updateTime', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
        ),
        migrations.AddField(
            model_name='intervaljob',
            name='interjob',
            field=models.ForeignKey(to='monManager.MonUnit'),
        ),
        migrations.AddField(
            model_name='cronjob',
            name='cronjob',
            field=models.ForeignKey(to='monManager.MonUnit'),
        ),
    ]
