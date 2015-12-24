#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from mysql.connector import (connection)
import time
import uuid

# 本地数据库连接配置
config_local = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'transcloudsso'
}

# 获取链接，获取游标
con_local = connection.MySQLConnection(**config_local)
cursor_local = con_local.cursor()

# 查询语句
query_sql_local = ("SELECT * FROM china")
cursor_local.execute(query_sql_local)

# 插入语句
add_dict = "INSERT INTO tc_auth_dict " \
           "(oid, pid, code_type, code_value, code_name, code_ename, valid, create_time, update_time) " \
           "VALUES " \
           "(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

# 构造数据
data_list = []
for (id, name, pid) in cursor_local:
    temp_uuid = str(uuid.uuid1()).split('-')
    temp_delimiter = ''
    temp_uuid = temp_delimiter.join(temp_uuid)
    # 数据
    temp_one = (
        temp_uuid, pid, 'district', id, name, '', '1', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    data_list.append(temp_one)

# 执行插入数据
cursor_local.executemany(add_dict, data_list)
con_local.commit()

# 关闭所有链接
cursor_local.close()
con_local.close()
