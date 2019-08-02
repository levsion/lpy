import os,sys

reload(sys)  
sys.setdefaultencoding('utf-8')

if len(sys.argv)<4:
    print "error wrong argv !!!, argv format like: start_process.py /usr/local/php71/bin/php a.php 10"
    quit()

bin_path = sys.argv[1]
file_path = sys.argv[2]
process_num = int(sys.argv[3])

exists_lines = os.popen('ps aux |grep \''+bin_path+' '+file_path+'\' |grep -v \'grep\'').readlines()
exists_num = len(exists_lines)
if (exists_num > process_num):
    quit()

process_num = process_num -exists_num
if exists_num>1:
    process_num = process_num+1
#print process_num
#quit()
for i in range(process_num):
    #os.system('nohup '+bin_path+' '+file_path+'>>/var/log/php/insert.log 2>>/var/log/php/insert_error.log &')
    os.system('docker exec myphp71 /bin/bash -c "nohup '+bin_path+' '+file_path+' >>/var/log/php/insert.log 2>>/var/log/php/insert_error.log &"')