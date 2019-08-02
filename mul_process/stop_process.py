import os,sys

reload(sys)  
sys.setdefaultencoding('utf-8')

if len(sys.argv)<2:
    print "error wrong argv !!!, argv format like: stop_process.py a.php"
    quit()

keyword = sys.argv[1]
os.system('ps -ef|grep '+keyword+'|grep -v grep|cut -c 9-15|xargs kill -9')