#!/usr/bin/env python
#coding:utf-8
from django.contrib import admin
from .models import *

admin.site.register(MonUnit)
admin.site.register(CronJob)
admin.site.register(IntervalJob)
admin.site.register(Errors)
admin.site.register(Status)
