# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 17:07:42 2017

@author: liuning11
"""

import datetimeUtil


def DoTest():
    print(str(datetimeUtil.tomorrow()))
    print(str(datetimeUtil.yesterday()))
    print('\n')

    print(datetimeUtil.datetimeStr_timestamp('2017-6-25 9:00:00'))
    print(
        datetimeUtil.datetimeStr_timestamp('2017-6-25 9:00:00',
                                           '%Y-%m-%d %H:%M:%S'))
    print(datetimeUtil.timestamp_datetime(1498352400.0, '%Y-%m-%d %H:%M:%S'))
    print('\n')

    print(
        datetimeUtil.datetime_timestamp(
            datetimeUtil.str_datetime('2017-6-25 9:00:00')))

    print('\n')
    print(
        datetimeUtil.subStr('2017-6-25 9:00:00', '2017-6-25 10:00:00',
                            '%Y-%m-%d %H:%M:%S'))
    print(str(datetimeUtil.addSec2ts(1498352400.0, 1)))


if __name__ == '__main__':
    DoTest()
