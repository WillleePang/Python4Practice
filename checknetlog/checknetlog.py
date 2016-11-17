#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import os


# 获取时间
result = ''
now = int(time.time())
result += "当前时间：%s \n" % now
errors = 0
with open('net.log', 'r') as f:
    for line in f:
        log_time = line[0:19]
        log_timestamp = int(time.mktime(time.strptime(log_time, "%Y-%m-%d %H:%M:%S")))
        if (now > log_timestamp) & ((now - log_timestamp) < 60):
            # print log_time
            # print line
            if "ERROR: Game take" in line:
                errors += 1
    result += "共筛选出：%s 行 \n" % errors
    if errors >= 20:
        return_code = os.system('/data/web/tomcat_tank_test/shutdown.sh')
        if return_code == 0:
            result += "关闭服务成功"
            os.system('/data/web/tomcat_tank_test/startup.sh')
            if return_code == 0:
                result += "启动服务成功"
            else:
                result += "启动服务失败"
        else:
            result += "关闭服务失败"

after = int(time.time())
result += "共耗时：%s \n" % (after-now)

with open('result.txt', 'w') as f:
    f.write(result)
