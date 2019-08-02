# incoding=utf-8
'''
run forever
'''

import time, os

crontab_file = '/usr/local/py/crontab/crontab.py'

while True:
    now_localtime = time.localtime()
    now_min = time.strftime("%M", now_localtime)
    now_second = time.strftime("%S", now_localtime)

    min_int = int(now_min)
    second_int = int(now_second)

    if second_int == 0:
        os.system("python " + crontab_file)

    time.sleep(1)
