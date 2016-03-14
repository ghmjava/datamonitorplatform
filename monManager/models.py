#!/usr/bin/env python
#!coding:utf-8

from django.db import models

# Create your models here.

WeekDays = (
        (u'mon', u'周一'),
        (u'tue', u'周二'),
        (u'wed', u'周三'),
        (u'thu', u'周四'),
        (u'fri', u'周五'),
        (u'sat', u'周六'),
        (u'sun', u'周日'),
        (u'*', '不指定')
        )

Categories = (
        (u'数据中心', u'datacenter'),
        (u'focus', u'focus'),
        (u'data报表', u'datareport')
        )

def genNumChoices(begin, end):
    res = []
    for i in range(begin,end+1):
        res.append((i,i))
    return tuple(res)

monthChoices = genNumChoices(0,12)
dayChoices = genNumChoices(0,31)
weekChoices = genNumChoices(0,53)
hourChoices = genNumChoices(0,23)
minuteChoices = genNumChoices(0,59)
secondChoices = genNumChoices(0,59)

class MonUnit(models.Model):
    funcName = models.CharField(max_length=200, unique=True, verbose_name=u'函数名')
    funcBody = models.TextField(verbose_name=u'函数主体')
    email = models.TextField(default='siweixu@meilishuo.com', verbose_name=u'报错通知邮箱地址，以逗号分隔')
    category = models.CharField(choices=Categories, unique=True, verbose_name=u'业务线')
    notes = models.TextField(default=u'备注', verbose_name=u'备注')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')

    def __unicode__(self):
        return self.funcName

class Status(models.Model):
    statusBody = models.OneToOneField(MonUnit, primary_key=True)
    status = models.CharField(max_length=20, verbose_name=u'监控状态')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    def __unicode__(self):
        return self.status.funcName

class Errors(models.Model):
    errBody = models.ForeignKey(MonUnit)
    errInfo = models.TextField(default=u'ERROR', verbose_name=u'ERROR')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')

class CronJob(models.Model):
    cronjob = models.ForeignKey(MonUnit)
    year = models.CharField(max_length=20, default='*', verbose_name=u'年(4位数字)', help_text="默认为*，更详细的表达式用法请参考<a href='http://redmine.meilishuo.com/projects/meilishuo-web/wiki/%E6%95%B0%E6%8D%AE%E6%B5%81%E7%9B%91%E6%8E%A7%E5%B9%B3%E5%8F%B0'>数据流监控平台wiki</a>")
    month = models.CharField(max_length=20, default='*', verbose_name=u'月')
    day = models.CharField(max_length=20, default='*', verbose_name=u'日')
    week = models.CharField(max_length=20, default='*', verbose_name=u'周')
    day_of_week = models.CharField(max_length=20, default='*', choices=WeekDays, verbose_name=u'一周中的哪天')
    hour = models.CharField(max_length=20, default='*', verbose_name=u'时')
    minute = models.CharField(max_length=20, default='*', verbose_name=u'分')
    second = models.CharField(max_length=20, default='*', verbose_name=u'秒')
    start_date = models.DateTimeField(default=None, verbose_name=u'任务启动时间')
    end_date = models.DateTimeField(default=None, verbose_name=u'任务持续到啥时结束')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updateTime = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')

    def __unicode__(self):
        return self.cronjob.funcName + "_cronjob"


class IntervalJob(models.Model):
    interjob = models.ForeignKey(MonUnit)
    weeks = models.IntegerField(default=0, verbose_name=u'间隔多少周')
    days = models.IntegerField(default=0, verbose_name=u'间隔多少天')
    hours = models.IntegerField(default=0, verbose_name=u'间隔多少小时')
    minutes = models.IntegerField(default=0, verbose_name=u'间隔多少分钟')
    seconds = models.IntegerField(default=0, verbose_name=u'间隔多少秒')
    start_date = models.DateTimeField(default=None, verbose_name=u'任务启动时间')
    end_date = models.DateTimeField(default=None, verbose_name=u'任务持续到啥时结束')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')
    updateTime = models.DateTimeField(auto_now=True,verbose_name=u'修改时间')

    def __unicode__(self):
        return self.interjob.funcName + "_intervaljob"

import logging
logging.basicConfig()
from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler(standalone=True)

class Jobs():
    def __init__(self):
        pass

jobs = Jobs()
