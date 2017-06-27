# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:56:37 2017

@author: liuning11
"""

from Task import Task
from TaskType import TaskType


def DoTest():
    ts = []
    ts.append(Task("测试1"))
    ts.append(Task("测试2"))
    for o in ts:
        print(o.name)
        print(o.type)


if __name__ == '__main__':
    DoTest()
