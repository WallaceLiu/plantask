# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 09:47:35 2017

@author: liuning11
"""
from base import base


class nodeProjectz(base):
    '''
    任务集合类
    '''

    def __init__(self):
        self.tasks = []

    #添加任务
    def add(self, t):
        self.tasks.append(t)

    # 输出
    def printer(self):
        pass


#        def p(self, p, i):
#            s = ''
#            for t in p.childs.tasks:
#                for j in range(i):
#                    s += '\t'
#                print(s + t.toString(False))
#                s = ''
#                if len(t.childs.tasks) > 0:
#                    p(self, t, i + 1)
#
#        i = 0
#        for t in self.tasks:
#            print(t.toString(True))
#            if len(t.childs.tasks) > 0:
#                p(self, t, i + 1)
