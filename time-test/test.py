import time
import calendar
import datetime

print "time stamp:", time.time()
print "local time:", time.localtime()
print("utc time:", time.gmtime())

# 时间戳
time_stamp = time.time()
# 时间戳转struct_time类型的本地时间
local_time = time.localtime(time_stamp)
# 时间戳转struct_time类型的utc时间
utc_time = time.gmtime(time_stamp)
# struct_time类型的本地时间转时间戳
time_stamp_1 = time.mktime(local_time)
# struct_time类型的utc时间转时间戳
time_stamp_2 = calendar.timegm(utc_time)
print(time_stamp, time_stamp_1, time_stamp_2)
# 时间戳转字符串(本地时间字符串)
print(time.ctime(time_stamp))
# struct_time类型的本地时间转字符串
print(time.asctime(local_time))
# struct_time类型的utc时间转字符串
print(time.asctime(utc_time))
# struct_time类型的本地时间转字符串：自定义格式
print(time.strftime("%Y-%m-%d, %H:%M:%S, %w", local_time))
# struct_time类型的utc时间转字符串：自定义格式
print(time.strftime("%Y-%m-%d, %H:%M:%S, %w", utc_time))
# 获取datetime.datetime类型的本地时间
a_datetime_local = datetime.datetime.now()
# 获取datetime.datetime类型的utc时间
a_datetime_utc = datetime.datetime.utcnow()
# datetime.datetime类型转字符串
print(a_datetime_local.strftime("%Y-%m-%d, %H:%M:%S, %w"))
# datetime.datetime类型转字符串
print(a_datetime_utc.strftime("%Y-%m-%d, %H:%M:%S, %w"))
# 字符串转datetime.datetime格式
a_datetime = datetime.datetime.strptime("2016-11-15, 15:32:12, 2", "%Y-%m-%d, %H:%M:%S, %w")
# 时间戳转字符串(本地时间字符串)
print(time.ctime(time_stamp))
# struct_time类型的本地时间转字符串
print(time.asctime(local_time))
# struct_time类型的utc时间转字符串
print(time.asctime(utc_time))
# struct_time类型的本地时间转字符串：自定义格式
print(time.strftime("%Y-%m-%d, %H:%M:%S, %w", local_time))
# struct_time类型的utc时间转字符串：自定义格式
print(time.strftime("%Y-%m-%d, %H:%M:%S, %w", utc_time))
# 字符串转struct_time类型
struct_time = time.strptime("2016-11-15, 15:32:12, 2", "%Y-%m-%d, %H:%M:%S, %w")
