#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import time
import os
from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


# 构建邮件内容
def makemsg(from_email, to_email):
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    msg = MIMEText('soket检查，连接异常，web正在重启中', 'plain', 'utf-8')
    msg['From'] = _format_addr(u'web用户 <%s>' % from_email)
    msg['To'] = _format_addr(u'管理员 <%s>' % to_email)
    msg['Subject'] = Header(u'web服务重启通知', 'utf-8').encode()
    return msg


# 发送邮件
def sendmail():
    # 输入Email地址和口令:
    from_email = 'zhanjianyonghu@sincetimes.com'
    password = '123qweQWE'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.sincetimes.com'
    # 输入SMTP服务器端口:
    smtp_port = '25'
    # 输入收件人地址:
    to_email_list = ['liu.huibin@sincetimes.com', 'sun.duo@sincetimes.com', 'jia.ruwen@sincetimes.com',
                     'zhang.zhirong@sincetimes', 'wang.rui@sincetimes.com', 'ye.qingyao@sincetimes.com',
                     'wang.hui@sincetimes.com', '1136185274@qq.com', '775047040@qq.com', '272978275@qq.com',
                     '272250571@qq.com', '512817196@qq.com', 'bobbyabby0001@163.com', 'wu.mengli@sincetimes.com']
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.set_debuglevel(1)
    server.login(from_email, password)
    for to_email in to_email_list:
        msg = makemsg(from_email, to_email)
        server.sendmail(from_email, to_email_list, msg.as_string())
    server.quit()


# 定义 输出日志函数
def writeLog(log):
    now_str = time.strftime("%Y-%m-%d", time.localtime(now))
    with open('result' + now_str + '.txt', 'a') as f:
        f.write(log)


# 获取时间
result = ''
now = int(time.time())
result = "当前时间：%s \n" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
writeLog(result)
errors = 0
with open('/data/logs/weblog/net.log', 'r') as f:
    for line in f:
        log_time = line[0:19]
        log_timestamp = int(time.mktime(time.strptime(log_time, "%Y-%m-%d %H:%M:%S")))
        if (now > log_timestamp) & ((now - log_timestamp) < 300):
            # print log_time
            # print line
            if "ERROR: Game take" in line:
                errors += 1
    result = "共筛选出：%s 行 \n" % errors
    writeLog(result)
    if errors >= 200:
        result = "检测服务出错，重启服务器"
        writeLog(result)
        writeLog("发送邮件")
        sendmail()
        writeLog("发送邮件完毕")
        return_code = os.system('/data/web/tomcat_tank/shutdown.sh')
        if return_code == 0:
            result = "关闭服务成功"
            writeLog(result)
            return_code = os.system('/data/web/tomcat_tank/startup.sh')
            if return_code == 0:
                result = "启动服务成功"
                writeLog(result)
            else:
                result = "启动服务失败"
                writeLog(result)
        else:
            result = "关闭服务失败"
            writeLog(result)
    else:
        result = "检测没有服务出错"
        writeLog(result)
after = int(time.time())
result = "共耗时：%s \n" % (after - now)
writeLog(result)
