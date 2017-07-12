# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author: liuning11
"""
from datetime import datetime
from datetime import timedelta
import time


# 时间戳转换成日期
# value 为时间戳，整型
# format 为日期格式，例如：%Y-%m-%d %H:%M:%S
def timestamp_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt


# 日期转换成时间戳 
# dt 为日期字符串
# format 日期格式，例如：%Y-%m-%d %H:%M:%S
def datetimeStr_timestamp(dtStr, format='%Y-%m-%d %H:%M:%S'):
    s = time.mktime(time.strptime(dtStr, format))
    return s


# 日期转换成时间戳 
# dt 为日期
# format 日期格式，例如：%Y-%m-%d %H:%M:%S
def datetime_timestamp(dt, format='%Y-%m-%d %H:%M:%S'):
    s = time.mktime(dt.timetuple())
    return s


# 字符串转换成日期
def str_datetime(str, format='%Y-%m-%d %H:%M:%S'):
    return datetime.strptime(str, format)


def datetime_str(dt, format='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(format)


def addDay(dt, d):
    aDay = timedelta(days=d)
    now = dt + aDay
    return now


# 增加秒
def addSec2ts(ts, s):
    dt = time.localtime(ts)
    d = datetime(dt.tm_year, dt.tm_mon, dt.tm_mday, dt.tm_hour, dt.tm_min,
                 dt.tm_sec)
    aSec = timedelta(seconds=s)
    now = d + aSec
    return time.mktime(now.timetuple())


# 昨天
def yesterday():
    now = datetime.now()
    return addDay(now, -1)


# 明天
def tomorrow():
    now = datetime.now()
    return addDay(now, 1)


# 相减
def sub(d1, d2):
    eclipseTimes = d2 - d1
    return eclipseTimes


# 相减
def subStr(d1Str, d2Str, format):
    d1 = str_datetime(d1Str, format)
    d2 = str_datetime(d2Str, format)
    return sub(d1, d2)
