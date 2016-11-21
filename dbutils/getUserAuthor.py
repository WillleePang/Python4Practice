#! /usr/bin/env python
# encoding: utf-8

from mysql.connector import (connection)
import time
import uuid

# 本地数据库连接配置
config_local = {
    'user': 'worldship',
    'password': 'worldship',
    'host': '203.195.217.45',
    'database': 'worldship_sso'
}


# 获取链接，获取游标
con_local = connection.MySQLConnection(**config_local)
cursor_local = con_local.cursor()

# 查询语句
query_sql_local = ("SELECT _user_id, _account,_name FROM user order by _account")
cursor_local.execute(query_sql_local)
user_list = []
for (id,account, name) in cursor_local:
    user_info = []
    user_info.append(id)
    user_info.append(account)
    user_info.append(name)
    user_list.append(user_info)

for user_info in user_list:
    query_sql_local = ("select b._name from user_auth_rel as a left join platform as b on a._platform_id = b._platform_id where a._user_id = "+str(user_info[0])+" and a._auth_type=1")
    cursor_local.execute(query_sql_local)
    platform_list=[]
    for (name) in cursor_local:
        platform_list.append(name)
    user_info.append(platform_list)


import codecs

f = codecs.open('result.txt','w','utf-16')
for user_info in user_list:
    content = user_info[1]+"|"
    content += user_info[2]+"|"
    for platform in user_info[3]:
        content += platform[0]+" "
    f.write(content+"\t\n")

f.close()
