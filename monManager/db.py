#!/usr/bin/env python

#coding:utf-8

import mysql.connector as mc
import hashlib
import simplejson as sj
import urllib,urllib2
import os,sys
import time, datetime
import traceback
import re


def takeDataFromMySQL(sql, database='focus', host='172.16.7.139', port=3307, user='mlsreader', password='RMlSxs&^c6OpIAQ1'):
    con = mc.connect(user=user, password=password, host=host, port=port, database=database)
    cur = con.cursor()
    try:
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        con.close()
        return res
    except:
        #traceback.print_exc()
        cur.close()
        con.close()

def buildDBInfo(MYSQLINI='/home/work/conf/real/bj/mysql/bi/bi.mysql.ini'):
    dbinfo = {}
    with open(MYSQLINI) as f:
        for line in f:
            res = re.search("db=(.*?)\s+host=(\d+\.\d+\.\d+\.\d+)\s+port=(\d{4})\s+weight=(\d)\s+user=(.*?)\s+pass=(.*?)\s+master=(\d)", line.strip('\n'))
            if res == None:
                print line 
                continue
            if len(res.groups()) == 7:
                if res.group(7) == '0':
                    dbinfo[res.group(1)] = {'database':res.group(1), 'host':res.group(2), 'port':int(res.group(3)), 'weight':res.group(4), 'user':res.group(5), 'password':res.group(6), 'master':res.group(7)}
    return dbinfo

DBINFO = buildDBInfo()

def query(sql, dbname, dbinfo=DBINFO):
    res = takeDataFromMySQL(sql, database=dbname, host=dbinfo[dbname]['host'], port=dbinfo[dbname]['port'], user=dbinfo[dbname]['user'], password=dbinfo[dbname]['password'])
    return res
    
def checkMySqlInfoUpdate(request, MYSQLINI='/home/work/conf/real/bj/mysql/bi/bi.mysql.ini'):
    timeStamp = time.ctime(os.stat(MYSQLINI).st_mtime)
    while True:
        newTimeStamp = time.ctime(os.stat(MYSQLINI).st_mtime)
        if newTimeStamp != timeStamp:
            print "Update DBINFO..."
            DBINFO = buildDBInfo()
            timeStamp = newTimeStamp

if __name__ == "__main__":
    dbinfo = buildDBInfo()
    #print dbinfo
    

    
