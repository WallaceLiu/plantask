# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:29:37 2017

@author: liuning11
"""
from datetime import datetime
import time


# 时间戳转换成日期
# value 为时间戳，整型
# format 为日期格式，例如：%Y-%m-%d %H:%M:%S
def timestamp_datetime(value, format):
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt


# 日期转换成时间戳 
# dt 为日期字符串
# format 日期格式，例如：%Y-%m-%d %H:%M:%S
def datetime_timestamp(dt, format):
    s = time.mktime(time.strptime(dt, format))
    return s

# 字符串转换成日期
def str_datetime(str, format):
    return datetime.strptime(str, format)
