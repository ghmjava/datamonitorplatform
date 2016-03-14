from django.shortcuts import render,get_object_or_404
from functools import partial
from .models import *
from .db import *
from .sendSMS import *
import traceback

def FAIL(msg,recipients,monUnit,send=1):
    sendSMS(msg,recipients,send)
    try:
        error = Errors(errBody=monUnit, errInfo=msg)
        error.save()
    except:
        traceback.print_exc()
        print >> sys.stderr, "Failed to write Error Info: ", msg

    try:
        res = Status.objects.get(statusBody=monUnit)
        if res:
            res.status = "FAIL"
        else:
            fail = Status(statusBody=monUnit, status="FAIL")
            fail.save()
    except:
        traceback.print_exc()
        print >> sys.stderr, "Failed to write FAIL INFO"
 

def SUCCESS(monUnit):
    try:
        res = Status.objects.get(statusBody=monUnit)
        if res
            res.status = "SUCCESS"
        else:
            suc = Status(statusBody=monUnit, status="SUCCESS")
            suc.save()
    except:
        traceback.print_exc()
        print >> sys.stderr, "Failed to write SUCCESS INFO"
