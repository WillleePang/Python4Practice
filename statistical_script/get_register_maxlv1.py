#! /usr/bin/env python
# -*- coding: UTF-8 -*-

file = open("templog_uid.txt", "r")
arr_uid = {}
while True:
    line = file.readline()
    if len(line) == 0:
        break
    paraList = line.split(",")
    arr_uid[paraList[1]] = 0
file.close()

print arr_uid

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
