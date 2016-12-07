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
    'database': 'worldship_sso_new'
}

# 获取链接，获取游标
con_local = connection.MySQLConnection(**config_local)
cursor_local = con_local.cursor()

# 插入语句
query_sql_local = ("SELECT _platform_id FROM platform order by _platform_id asc")
cursor_local.execute(query_sql_local)
platform_ids = []
for (id,) in cursor_local:
    platform_ids.append(id)

print platform_ids

# 插入语句
add_dict = "INSERT INTO role " \
           "(_name, _platform_id) " \
           "VALUES " \
           "( %s, %s)"
# 构造数据
data_list = []
for (id) in platform_ids:
    for name in ['全部权限', '代理权限']:
        # 数据
        temp_one = (name, id)
        data_list.append(temp_one)

# 执行插入数据
cursor_local.executemany(add_dict, data_list)
con_local.commit()

# 关闭所有链接
cursor_local.close()
con_local.close()
