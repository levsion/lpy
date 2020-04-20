#!/usr/bin/env python 
import os,sys,time

if len(sys.argv)>1:
	file_path = sys.argv[1]
else:
	now_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = now_dir + '/' + 'new_log.py'
if not os.path.isfile(file_path):
	print("Error: newlog file not exists !!!")
	quit()

port_list = ['5151','5152']
if(len(port_list)<1):
	quit()
for port in port_list:
	try:
		#ret = os.popen('ps aux |grep \''+file_path+' '+port+'\' |grep -v \'grep\'').readlines()
		ret = os.popen('ps aux |grep \'new_log.py '+port+'\' |grep -v \'grep\'').readlines()
		#print ret
		if len(ret)<1:
			print("process killed then start:",port)
			os.system("nohup python3 "+file_path+" "+port+" >/tmp/new_log_"+port+".log 2>&1 &")
	except:
		print("Error", sys.exc_info()[1])
