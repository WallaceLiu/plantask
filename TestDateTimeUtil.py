# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:07:42 2017

@author: liuning11
"""

import DateTimeUtil


def DoTest():
    print(str(DateTimeUtil.tomorrow()))
    print(str(DateTimeUtil.yesterday())) 
    print('\n')
    print(
        DateTimeUtil.datetime_timestamp('2017-6-25 9:00:00',
                                        '%Y-%m-%d %H:%M:%S'))
    print(
        DateTimeUtil.subStr('2017-6-25 9:00:00', '2017-6-25 10:00:00',
                            '%Y-%m-%d %H:%M:%S'))     
    print(DateTimeUtil.datetime_timestamp('2017-6-25 9:00:00','%Y-%m-%d %H:%M:%S'))
    print(DateTimeUtil.timestamp_datetime(1498352400.0,'%Y-%m-%d %H:%M:%S'))
    
    print(str(DateTimeUtil.addSecond2ts(1498352400.0,1)))
    #print(DateTimeUtil.addSecond2ts(,1))


if __name__ == '__main__':
    DoTest()