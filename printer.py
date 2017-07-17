# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 09:47:35 2017

@author: liuning11
"""


class printer:
    '''
    任务集合类
    '''

    def __init__(self):
        pass

    '''
    打印
    '''

    def printerBrief(self):
        def p(self, p, i):
            s = ''
            for t in p.childs.tasks:
                for j in range(i):
                    s += '\t'
                print(s + t.toStringBrief())
                s = ''
                if len(t.childs.tasks) > 0:
                    p(self, t, i + 1)

        i = 0
        for t in self.tasks:
            print(t.toStringBrief())
            if len(t.childs.tasks) > 0:
                p(self, t, i + 1)

    def printer(self):
        def p(self, p, i):
            s = ''
            for t in p.childs.tasks:
                for j in range(i):
                    s += '\t'
                print(s + t.toString(False))
                s = ''
                if len(t.childs.tasks) > 0:
                    p(self, t, i + 1)

        i = 0
        for t in self.tasks:
            print(t.toString(True))
            if len(t.childs.tasks) > 0:
                p(self, t, i + 1)
