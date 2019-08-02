# incoding=utf-8
'''
run once per minute
'''

import hashlib
import sys, os
import time, random, re
import thread, threading

reload(sys)
sys.setdefaultencoding('utf-8')


class myThread(threading.Thread):
    def __init__(self, threadID, name, cmd):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.cmd = cmd

    def run(self):
        # print "Starting " + self.name
        cmdGo(self.name, self.cmd)
    # print "Exiting " + self.name


def cmdGo(threadName, cmd):
    os.system(cmd)


# print "%s: %s" % (threadName, time.ctime(time.time()))


cmd_file = '/usr/local/py/crontab/cmd.ini'
if not os.path.exists(cmd_file):
    print ("%s file not exist !!!" % cmd_file)
    quit()

cmd_list = []
with open(cmd_file, 'r') as f:
    for line in f.readlines():
        line = line.strip().replace('\ufeff', '')
        if len(line) > 0:
            cmd_list.append(line)

if len(cmd_list) <= 0:
    print ("can't find any cmd in file:%s !!!" % cmd_file)
    quit()

# start go
now_localtime = time.localtime()
now_year = time.strftime("%Y", now_localtime)
now_month = time.strftime("%m", now_localtime)
now_day = time.strftime("%d", now_localtime)
now_hour = time.strftime("%H", now_localtime)
now_min = time.strftime("%M", now_localtime)
now_second = time.strftime("%S", now_localtime)
now_week = time.strftime("%w", now_localtime)

min_int = int(now_min)
second_int = int(now_second)
hour_int = int(now_hour)
day_int = int(now_day)
month_int = int(now_month)
week_int = int(now_week)
'''
if second_int%10==0:
	ret = os.popen('ps aux |grep \'/usr/sbin/hehe.sh\' |grep -v \'grep\'').readlines()
	if len(ret)<1:
		os.system("sh /usr/sbin/hehe.sh")
'''
now_list = [min_int, hour_int, day_int, month_int, week_int]
for cmd_line in cmd_list:
    str_list_old = cmd_line.split(' ')
    str_list = []
    for i in range(len(str_list_old)):
        str_tmp = str_list_old[i].replace(' ', '')
        if len(str_tmp) > 0:
            str_list.append(str_tmp)
    if len(str_list) < 6:
        continue
    time_list = str_list[0:5]
    cmd = ' '.join(str_list[5:])
    # print time_list,cmd
    cmd_go = True
    for i in range(len(time_list)):
        if (time_list[i] != '*') and (not re.match(r'\*\/[0-9]+', time_list[i], re.I)) and (not re.match(r'[0-9]+', time_list[i])) and (not re.match(r'([0-9]+,?)+', time_list[i])):
            # print 'a',i,time_list[i]
            cmd_go = False
            break
        if len(time_list[i]) == 1 and time_list[i] != '*' and int(time_list[i]) != now_list[i]:
            # print 'c',i,time_list[i]
            cmd_go = False
            break
        elif (re.match(r'\*\/[0-9]+', time_list[i])) and (now_list[i] % int(time_list[i][2]) != 0):
            # print 'd',i,time_list[i]
            cmd_go = False
            break
        elif re.match(r'([0-9]+,?)+', time_list[i]):
            t_list = time_list[i].split(',')
            if not (str(now_list[i]) in t_list):
                # print 'e',i,time_list[i]
                cmd_go = False
                break
    if cmd_go:
        # print 'cmd go go go: ',cmd
        thread1 = myThread(random.randint(1000, 9999), str(random.randint(1000, 9999)), cmd)
        thread1.start()
