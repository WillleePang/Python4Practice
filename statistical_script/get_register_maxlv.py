#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import os, glob, sys

# python get_register_maxlv.py '20160316' '20160322' '117'
start_time = sys.argv[1]
end_time = sys.argv[2]
channel = sys.argv[3]
print start_time, end_time, channel
print 'initing log file!'
os.system('''rm -f templog.txt''')
os.system('''rm -f templog_uid.txt''')
os.system('''rm -f templog_level.txt''')
os.system('''rm -f templog_result.txt''')
print 'initing log file complete!'

print 'analyzing log file!'
for log_file in glob.glob("LogStat_*.log"):
    if int(log_file[8:-8].replace('-', '')) in range(int(start_time), int(end_time)):
        os.system(
            '''cat ''' + log_file + ''' | grep '^2016-*' |grep 'Register' | awk -F "," '{OFS=","; if($11 == ''' + channel + ''') print $1,$3,$5,$11}' >> templog.txt''')
print 'analyze log file complete!'

print 'generating templog_uid.txt!'
os.system('''cat templog.txt | awk '!a[$2]++{print $1,$2,$3,$4}' > templog_uid.txt''')
print 'generate templog_uid.txt complete!'

os.system('''rm -f templog.txt''')

print 'analyzing log file!'
for log_file in glob.glob("LogStat_*.log"):
    if int(log_file[8:-8].replace('-', '')) in range(int(start_time), int(end_time)):
        os.system(
            '''cat ''' + log_file + ''' | grep '^2016-*' | awk -F "," '{OFS=","; if($11 == ''' + channel + ''') print $1,$3,$5,$11}' >> templog.txt''')
print 'analyze log file complete!'

print 'generating templog_level.txt!'
os.system('''cat templog.txt | awk '!a[$2,$3]++{print $1,$2,$3,$4}' > templog_level.txt''')
print 'generate templog_level.txt complete!'

print 'generate templog_result.txt!'
file = open("templog_uid.txt", "r")
arr_uid = {}
while True:
    line = file.readline()
    if len(line) == 0:
        break
    paraList = line.split(",")
    arr_uid[paraList[1]] = 0
file.close()

file = open("templog_level.txt", "r")
while True:
    line = file.readline()
    if len(line) == 0:
        break
    paraList = line.split(",")
    uid = paraList[1]
    level = paraList[2]
    if uid in arr_uid:
        level_num = int(level)
        if level_num >= arr_uid[uid]:
            arr_uid[uid] = level_num
file.close()

file = open('templog_result.txt', 'w')
for key, value in arr_uid.items():
    file.write(key + "," + str(value) + "\n")
file.close()
print 'generate templog_result.txt complete!'
