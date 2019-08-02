#!/usr/bin/env python 
import os,sys,time,commands
file_path = '/usr/local/lpy/newlog/new_log.py'
port_list = ['5151','5152']
if(len(port_list)<1):
	quit()
for port in port_list:
	try:
		#ret = os.popen('ps aux |grep \''+file_path+' '+port+'\' |grep -v \'grep\'').readlines()
		ret = os.popen('ps aux |grep \'new_log.py '+port+'\' |grep -v \'grep\'').readlines()
		#print ret
		if len(ret)<1:
			print "process killed then start:",port
			os.system("nohup python "+file_path+" "+port+" >/tmp/new_log_"+port+".log 2>&1 &") 
	except:
		print "Error", sys.exc_info()[1]
