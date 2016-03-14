from django.shortcuts import render,get_object_or_404
from functools import partial
from .models import *
from .db import *
from .sendSMS import *
import traceback
# Create your views here.

def debugPython():
    pass

def index(request):
    datacenters = Status.objects.filter(statusBody__category=u'datacenter')
    focuses = Status.objects.filter(statusBody__category=u'focus')
    datareports = Status.objects.filter(statusBody__category=u'datareport')

    datacentersSUC = Status.objects.filter(statusBody__category=u'datacenter').filter(status="FAIL")
    focusesSUC = Status.objects.filter(statusBody__category=u'focus').filter(status="FAIL")
    datareportsSUC = Status.objects.filter(statusBody__category=u'datareport').filter(status="FAIL")

    datacentersFAIL = Status.objects.filter(statusBody__category=u'datacenter').filter(status="SUCCESS")
    focusesFAIL = Status.objects.filter(statusBody__category=u'focus').filter(status="SUCCESS")
    datareportsFAIL = Status.objects.filter(statusBody__category=u'datareport').filter(status="SUCCESS")


    context = {'datacenters':datacenters, 'focuses':focuses, 'datareports':datareports, 'datacentersSUC':datacentersSUC, 'focusesSUC':focusesSUC, 'datareportsSUC':datareportsSUC, 'datacentersFAIL':datacentersFAIL, 'focusesFAIL':focusesFAIL, 'datareportsFAIL':datareportsFAIL}
    return render(request, 'monManager/index.html', context)
    

def addCronJob(sched,jobName):
    monunit = get_object_or_404(MonUnit, funcName=jobName)
    tmpbodylines = monunit.funcBody.split('\n')
    for i in xrange(len(tmpbodylines)):
        tmpbodylines[i] = '    ' + tmpbodylines[i]

    funcStr = "def " + monunit.funcName + '():\n' + '\n'.join(tmpbodylines)
    funcStr = funcStr + "\njobs." + monunit.funcName + " = " + monunit.funcName 
    print funcStr
    exec(funcStr)
    func = getattr(jobs, monunit.funcName)
    try:
        cronjob = CronJob.objects.get(cronjob__funcName=jobName)
    except:
        traceback.print_exc()
        cronjob = None
    cjob = None
    if cronjob:
        print "add cronjob ...", monunit.funcName+'_cron'
        cjob = sched.add_job(func, 'cron', year=cronjob.year, month=cronjob.month, day=cronjob.day, week=cronjob.week, day_of_week=cronjob.day_of_week, hour=cronjob.hour, minute=cronjob.minute, second=cronjob.second, start_date=cronjob.start_date, end_date=cronjob.end_date, id=monunit.funcName+'_cron', max_instances=100)
        cjob.resume()
        print "DEBUG cjob: ", cjob

    sched.print_jobs()
    return [cronjob, cjob]


def addIntervalJob(sched,jobName):
    monunit = get_object_or_404(MonUnit, funcName=jobName)
    tmpbodylines = monunit.funcBody.split('\n')
    for i in xrange(len(tmpbodylines)):
        tmpbodylines[i] = '    ' + tmpbodylines[i]

    funcStr = "def " + monunit.funcName + '():\n' + '\n'.join(tmpbodylines)
    funcStr = funcStr + "\njobs." + monunit.funcName + " = " + monunit.funcName 
    print funcStr
    exec(funcStr)
    func = getattr(jobs, monunit.funcName)
    try:
        intervaljob = IntervalJob.objects.get(interjob__funcName=jobName)
    except:
        #traceback.print_exc()
        intervaljob = None
    ijob = None
    if intervaljob:
        print "add intervaljob ...", monunit.funcName+'_interval'
        ijob = sched.add_job(func, 'interval', weeks=intervaljob.weeks, days=intervaljob.days, hours=intervaljob.hours, minutes=intervaljob.minutes, seconds=intervaljob.seconds, start_date=intervaljob.start_date, end_date=intervaljob.end_date, id=monunit.funcName+'_interval', max_instances=100)
        ijob.resume()

    sched.print_jobs()
    return [intervaljob, ijob]


def loop(para):
    print "DEBUG:", para
    mons = {}
    cronjobs = {}
    interjobs = {}
    try:
        print "Starting scheduler..."
        #sched.shutdown()
        sched.start()
        print "Finish starting"
    except(KeyboardInterrupt):
        traceback.print_exc()
        sched.shutdown(wait=False)
    while True:
        monunits = MonUnit.objects.all()
        for monunit in monunits:
            #global sendWarn
            #sendWarn = partial(sendSMS, recipients=monunit.email, monUnit=monunit)
            global fail
            fail = partial(FAIL, recipients=monunit.email, monUnit=monunit)
            global success
            success = partial(SUCCESS, monUnit=monunit)
            if monunit.funcName not in mons.keys():
                mons[monunit.funcName] = monunit
            if monunit.funcName not in cronjobs.keys():
                print "ADD Cron Job: ", monunit.funcName
                cjobres = addCronJob(sched, monunit.funcName)
                cronjobs[monunit.funcName] = [monunit, ] + cjobres
            else:
                try:
                    cronjob = CronJob.objects.get(cronjob__funcName=monunit.funcName)
                except:
                    cronjob = None
                if cronjob == None and cronjobs[monunit.funcName][1] == None:
                    pass
                elif cronjob == None and cronjobs[monunit.funcName][1] != None:
                    cronjobs[monunit.funcName][2].remove()
                elif cronjob != None and cronjobs[monunit.funcName][1] == None:
                    cjobres = addCronJob(sched, monunit.funcName)
                    cronjobs[monunit.funcName] = [monunit, ] + cjobres
                elif cronjob.updateTime != cronjobs[monunit.funcName][1].updateTime:
                    cronjobs[monunit.funcName][2].reschedule(trigger='cron', year=cronjob.year, month=cronjob.month, day=cronjob.day, week=cronjob.week, day_of_week=cronjob.day_of_week, hour=cronjob.hour, minute=cronjob.minute, second=cronjob.second, start_date=cronjob.start_date, end_date=cronjob.end_date)
                elif mons[monunit.funcName].updateTime != monunit.updateTime:
                    cronjobs[monunit.funcName][2].remove()
                    cjobres = addCronJob(sched, monunit.funcName)
                    cronjobs[monunit.funcName] = [monunit, ] + cjobres
                cronjobs[monunit.funcName][1] = cronjob
            if monunit.funcName not in interjobs.keys():
                ijobres = addIntervalJob(sched, monunit.funcName)
                interjobs[monunit.funcName] = [monunit, ] + ijobres
            else:
                try:
                    intervaljob = IntervalJob.objects.get(interjob__funcName=monunit.funcName)
                except:
                    intervaljob = None
                if intervaljob == None and interjobs[monunit.funcName][1] == None:
                    print "DEBUG intervaljob 1"
                    pass
                elif intervaljob == None and interjobs[monunit.funcName][1] != None:
                    print "DEBUG intervaljob 2"
                    interjobs[monunit.funcName][2].remove()
                elif intervaljob != None and interjobs[monunit.funcName][1] == None:
                    print "DEBUG intervaljob 3"
                    ijobres = addIntervalJob(sched, monunit.funcName)
                    interjobs[monunit.funcName] = [monunit, ] + ijobres               
                elif intervaljob.updateTime != interjobs[monunit.funcName][1].updateTime:
                    print "DEBUG intervaljob 4"
                    interjobs[monunit.funcName][2].reschedule(trigger='interval', weeks=intervaljob.weeks, days=intervaljob.days, hours=intervaljob.hours, minutes=intervaljob.minutes, seconds=intervaljob.seconds, start_date=intervaljob.start_date, end_date=intervaljob.end_date,)
                elif mons[monunit.funcName].updateTime != monunit.updateTime:
                    print "DEBUG intervaljob 5"
                    interjobs[monunit.funcName][2].remove()
                    ijobres = addIntervalJob(sched, monunit.funcName)
                    interjobs[monunit.funcName] = [monunit, ] + ijobres
                interjobs[monunit.funcName][1] = intervaljob
            mons[monunit.funcName] = monunit






