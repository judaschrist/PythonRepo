'''
Created on 2013-11-9

@author: zhanglinxiao 
'''

import urllib.request
import os
import time
from datetime import datetime
import threading

URLS = {}
# URLS['test'] = "http;//www.baidu.com"
URLS['eclipse'] = "https://bugs.eclipse.org/bugs/report.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED&resolution=---&resolution=FIXED&resolution=INVALID&resolution=WONTFIX&resolution=DUPLICATE&resolution=WORKSFORME&resolution=MOVED&resolution=NOT_ECLIPSE&x_axis_field=resolution&y_axis_field=bug_status&width=1024&height=600&action=wrap&ctype=csv&format=table"
URLS['kernel'] = "https://bugzilla.kernel.org/report.cgi?bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=REJECTED&bug_status=DEFERRED&bug_status=NEEDINFO&bug_status=CLOSED&resolution=---&resolution=CODE_FIX&resolution=PATCH_ALREADY_AVAILABLE&resolution=INVALID&resolution=WILL_NOT_FIX&resolution=WILL_FIX_LATER&resolution=DUPLICATE&resolution=UNREPRODUCIBLE&resolution=DOCUMENTED&resolution=INSUFFICIENT_DATA&resolution=MOVED&resolution=OBSOLETE&x_axis_field=resolution&y_axis_field=bug_status&width=1024&height=600&action=wrap&ctype=csv&format=table"
URLS['mozilla'] = "https://bugzilla.mozilla.org/report.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED&resolution=---&resolution=FIXED&resolution=INVALID&resolution=WONTFIX&resolution=DUPLICATE&resolution=WORKSFORME&resolution=INCOMPLETE&resolution=SUPPORT&resolution=EXPIRED&resolution=MOVED&x_axis_field=resolution&y_axis_field=bug_status&width=600&height=350&action=wrap&ctype=csv&format=table"
URLS['kde'] = "https://bugs.kde.org/report.cgi?bug_status=UNCONFIRMED&bug_status=CONFIRMED&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=RESOLVED&bug_status=NEEDSINFO&bug_status=VERIFIED&bug_status=CLOSED&resolution=---&resolution=FIXED&resolution=INVALID&resolution=WONTFIX&resolution=LATER&resolution=REMIND&resolution=DUPLICATE&resolution=WORKSFORME&resolution=MOVED&resolution=UPSTREAM&resolution=DOWNSTREAM&resolution=WAITINGFORINFO&resolution=BACKTRACE&resolution=UNMAINTAINED&x_axis_field=resolution&y_axis_field=bug_status&width=600&height=350&action=wrap&ctype=csv&format=table"
URLS['apache'] = "https://issues.apache.org/bugzilla/report.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&bug_status=NEEDINFO&bug_status=RESOLVED&bug_status=VERIFIED&bug_status=CLOSED&resolution=---&resolution=FIXED&resolution=INVALID&resolution=WONTFIX&resolution=LATER&resolution=REMIND&resolution=DUPLICATE&resolution=WORKSFORME&resolution=MOVED&x_axis_field=resolution&y_axis_field=bug_status&width=1024&height=600&action=wrap&ctype=csv&format=table"
DIR = 'data_per_day'
RETRY_NUM = 5

if not os.path.exists(DIR):
    os.mkdir(DIR)

def add_to_bugfile(name, data):
    bugfile = open(DIR + "/" + name + '.csv', mode='a')
#     print(data)
    bugfile.write(data)

def update_bug_num(name, url):
    print("UBDATING " + name + " FROM " + url)
    for i in range(RETRY_NUM):  
        try:
#             raise KeyboardInterrupt
            res = urllib.request.urlopen(url)    
            data = res.read().decode("utf-8")
            break
        except:
            print('RETRYING ' + str(i) + '...')
    else:
        print('FAIL TO UPDATE ' + name)
        return
    
    time = str(datetime.now())
    data = time + data[data.find(","):] + '\n'
    add_to_bugfile(name, data)
    

class BugUpdator(threading.Thread):
    def run(self):
        print(str(datetime.now()))
        for name, url in URLS.items():
            update_bug_num(name, url)

class Test(threading.Thread):
    def run(self):
        for i in range(3):
            print(i)
            time.sleep(1)

while True:
    updator = BugUpdator()
    updator.start()
    time.sleep(3600*24)
    




