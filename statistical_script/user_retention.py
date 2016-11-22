#! /usr/bin/env python
# -*- coding: UTF-8 -*-


import os
import sys

channel = sys.argv[1]

# cat LogStat_2016-11-15* |grep -i register| awk -F"," '{OFS=",";if($11 == 12103) print $3}'
os.system('''cat /data/stat/Log/LogStat_2016-11-15* |grep -i register| awk -F"," '{OFS=",";if($11 == ''' + channel +
          ''') print $3}' >> python_register.txt''')

os.system('''cat /data/stat/Log/LogStat_2016-11-16* |grep -i logon| awk -F"," '{OFS=",";if($11 == ''' + channel +
          ''') print $3}' >> python_active.txt''')


f = open("python_register.txt", "r")
uid1 = []
while True:
    line = f.readline()
    if len(line) == 0:
        break
    uid1.append(str(line))
f.close()

f = open("python_active.txt", "r")
uid2 = []
while True:
    line = f.readline()
    if len(line) == 0:
        break
    uid2.append(str(line))
f.close()
a = len(set(uid1))
b = len(list(set(uid1).intersection(set(uid2))))
result = "register：%d  useractive:%d \t" % (a, b)
f = open("result.txt", "w")
f.write(result)




