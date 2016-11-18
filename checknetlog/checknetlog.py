#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import smtplib
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
    msg = MIMEText('请尽快联系管理员，登录服务器进行修复！', 'plain', 'utf-8')
    msg['From'] = _format_addr(u'<%s>' % from_email)
    msg['To'] = _format_addr(u'<%s>' % to_email)
    msg['Subject'] = Header(u'服务器出现大量登录失败情况', 'utf-8').encode()
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
    to_email_list = ['liu.huibin@sincetimes.com', '1252248561@qq.com']
    server = smtplib.SMTP(smtp_server, smtp_port)
    # server.set_debuglevel(1)
    server.login(from_email, password)
    for to_email in to_email_list:
        msg = makemsg(from_email, to_email)
        server.sendmail(from_email, to_email_list, msg.as_string())
    server.quit()

# 获取时间
result = ''
now = int(time.time())
result += "定时任务开始============================================================\n"
result += "当前时间：%s \n" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
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
    # if errors >= 20:
    #     return_code = os.system('/data/web/tomcat_tank_test/shutdown.sh')
    #     if return_code == 0:
    #         result += "关闭服务成功"
    #         os.system('/data/web/tomcat_tank_test/startup.sh')
    #         if return_code == 0:
    #             result += "启动服务成功"
    #         else:
    #             result += "启动服务失败"
    #     else:
    #         result += "关闭服务失败"

after = int(time.time())
result += "共耗时：%s \n" % (after-now)
result += "发送邮件\n"
sendmail()
result += "定时任务结束============================================================\n"

# 写入日志
now_str = time.strftime("%Y-%m-%d", time.localtime(now))
with open('result'+now_str+'.txt', 'a') as f:
    f.write(result)



