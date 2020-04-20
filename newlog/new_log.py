# incoding=utf-8

import socket  
import struct  
import hashlib  
import sys,os
import time
import signal
import logging,string
import importlib

importlib.reload(sys)

g_server_host = ''
if len(sys.argv)<2:
    print("no port input, quit...")
    quit()
g_server_port = sys.argv[1]
if(not g_server_port or not (str(g_server_port).isdigit())):
    print("input wrong port, quit...")
    quit()
else:
	g_server_port = int(g_server_port)
g_server_log_path = '/var/log/newlog/'+str(g_server_port)
g_server_log_maxsize = 100*1024*1024

def MyLog(msg,fileaddr):
	'''new_log = logging.getLogger('new_log')
	file_handler = logging.FileHandler(fileaddr)
	file_handler.setLevel(logging.INFO)
	file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
	new_log.addHandler(file_handler)
	new_log.info(msg);
	'''
	#logging.basicConfig重复配置失效问题解决:
	'''if not os.path.exists(fileaddr):
		root = logging.getLogger()
		if root.handlers:
			for handler in root.handlers:
				root.removeHandler(handler)
	logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename=fileaddr,filemode='a')
	logging.info('['+str(time.time())+'] '+msg)'''
	fb = open(fileaddr,'a')
	now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	now_str = str(time.time())
	fb.write(now+" ["+now_str+"] "+msg+"\n")
	fb.close()

def PipeHandle(sigs,id):
	MyLog('sigs:'+sigs+' id:'+id,'/tmp/new_log1.log')
	pass

class LogServer(object):  
	def __init__(self):  
		self.socket = None
		signal.signal(signal.SIGPIPE,PipeHandle)
	def start(self):  
		print('LogServer Start!')
		global g_server_host
		global g_server_port
		global g_server_log_path
		global g_server_log_maxsize
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
		self.socket.bind((g_server_host,g_server_port))
		while True:
			data, address = self.socket.recvfrom(2500)
			if not data:
				#time.sleep(0.05)
				continue
			data_list = data.split(']')
			channel = data_list[0].lstrip('[')
			channel_dir = g_server_log_path+'/'+channel
			if not os.path.exists(channel_dir):
				continue
			now_localtime = time.localtime()
			now_year = time.strftime("%Y", now_localtime)
			now_month = time.strftime("%m", now_localtime)
			now_day = time.strftime("%d", now_localtime)
			now_hour = time.strftime("%H", now_localtime)
			now_min = time.strftime("%M", now_localtime)
			now_second = time.strftime("%S", now_localtime)
			file_dir = channel_dir+'/'+now_year+'/'+now_month+'/'+now_day
			if not os.path.exists(file_dir):
				try:
					os.makedirs(file_dir)
				except:
					continue
			log_path = self.getLogPath(file_dir);
			MyLog(data,file_dir+'/'+log_path)
			del data
			del address
			del log_path
			del data_list
			#time.sleep(0.05)
	def getLogPath(self,log_dir):
		if(not os.path.exists(log_dir)):
			return False
		list_file = os.listdir(log_dir)
		last_log = ''
		now_localtime = time.localtime()
		now_year = time.strftime("%Y", now_localtime)
		now_month = time.strftime("%m", now_localtime)
		now_day = time.strftime("%d", now_localtime)
		now_hour = time.strftime("%H", now_localtime)
		now_min = time.strftime("%M", now_localtime)
		now_second = time.strftime("%S", now_localtime)
		global g_server_log_maxsize
		for filename in list_file:
			if(filename[-4:]=='.log' and filename[:8]==now_year+now_month+now_day):
				if(os.path.getsize(log_dir+'/'+filename)<g_server_log_maxsize and len(filename)==18):
					return filename

		return now_year+now_month+now_day+now_hour+now_min+now_second+'.log'
		
  
if __name__ == "__main__":  
	server = LogServer()  
	server.start() 
	#MyLog('hehe','/tmp/new_log1.log');
