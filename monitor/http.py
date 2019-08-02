# incoding=utf-8
'''
monitor every http requests
'''

import os, sys, time, random
import threading
import ast
import urllib, urllib2

reload(sys)
sys.setdefaultencoding('utf-8')


class MyThread(threading.Thread):
    def __init__(self, threadID, name, url, code, request_type, request_data):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.url = url
        self.code = code
        self.request_type = request_type
        self.request_data = request_data

    def run(self):
        # print "Starting " + self.name
        cmdGo(self.name, self.url, self.code, self.request_type, self.request_data)


def cmdGo(threadName, url, code, request_type, request_data):
    now_localtime = time.localtime()
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", now_localtime)
    headers = {"User-Agent": "Monitor http"}
    try:
        if request_type == 'get' or (not request_data):
            request = urllib2.Request(url, headers=headers)
        else:
            data = urllib.urlencode(request_data)
            request = urllib2.Request(url, data=data, headers=headers)

        response = urllib2.urlopen(request, timeout=10)
        return_code = int(response.getcode())
        # return_str = response.read()
        # print return_str,'return_str'
        if return_code != code:
            print time_str, "url: %s , error_code: %d" % (url, return_code)
    except Exception as err:
        print time_str, "url: %s , error_msg: %s" % (url, err)
        quit()


cmd_file = '/usr/local/py/monitor/cmd.ini'
if not os.path.exists(cmd_file):
    print ("%s file not exist !!!" % cmd_file)
    quit()

cmd_list = []
with open(cmd_file, 'r') as f:
    for line in f.readlines():
        line = line.strip().replace('\ufeff', '')
        if len(line) > 0 and line[0:4] == 'http':
            cmd_list.append(line)

if len(cmd_list) <= 0:
    print ("can't find any cmd in file:%s !!!" % cmd_file)
    quit()

for cmd_line in cmd_list:
    str_list_old = cmd_line.split(' ')
    str_list = []
    for i in range(len(str_list_old)):
        str_tmp = str_list_old[i].replace(' ', '')
        if len(str_tmp) > 0:
            str_list.append(str_tmp)
    url = str_list[0]
    if len(str_list) > 1:
        code = int(str_list[1])
    else:
        code = 200
    if len(str_list) > 2:
        request_type = str_list[2]
    else:
        request_type = 'get'
    if len(str_list) > 3:
        request_str = ' '.join(str_list[3:])
        request_data = ast.literal_eval(request_str)
    else:
        request_data = {}

    thread1 = MyThread(random.randint(1000, 9999), str(random.randint(1000, 9999)), url, code, request_type, request_data)
    thread1.start()
