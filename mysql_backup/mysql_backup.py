#!/usr/bin/env python
#coding=utf-8


import sys,os,random,time,datetime

def MyLog(msg,fileaddr):
	fb = open(fileaddr,'a')
	now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	now_str = str(time.time())
	fb.write(now+" ["+now_str+"] "+msg+"\n")
	fb.close()

reload(sys)
sys.setdefaultencoding('utf-8')

mysql_host = '127.0.0.1'
mysql_port = 3306
mysql_user = 'root'
mysql_password = 'levsion123'
backup_dir = '/data/mysql/backup/'
database = ['gameweb','gameadmin']

mysql_dump_dir = ''

#docker exec -i mymysql sh -c 'exec mysqldump -database databasename -uroot -p"levsion123"' > /data/all-databases.sql

#mysqldump -hhostname -uusername -ppassword -database databasename | gzip > backupfile.sql.gz

for db in database:
	backup_name = db+'_'+time.strftime("%Y%m%d%H%M", time.localtime())+'.sql.gz'
	os.system('docker exec -i mymysql sh -c \'exec mysqldump --databases '+db+' -u'+mysql_user+' -p"'+mysql_password+'" |gzip\' > '+backup_dir+backup_name)
	MyLog('backup '+db+' success!  file address: '+backup_dir+backup_name,'/data/mysql/backup.log')

