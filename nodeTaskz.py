# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 09:47:35 2017

@author: liuning11
"""
from stageType import stageType


class nodeTaskz:
    '''
    任务集合类
    '''

    def __init__(self):
        self.tasks = []

    #添加任务
    def add(self, t):
        if self.isExist(t) == False:
            self.tasks.append(t)

    #判断任务是否存在
    def isExist(self, t):
        for task in self.tasks:
            if t.id == task.id:
                return True

        return False

    # 根据任务ID查找任务
    def findRootTask(self, id):
        for t in self.tasks:
            if t.id == id:
                return t

    # 根据任务编号查找任务，任务编号所有节点唯一
    def findTask(self, no):
        def find(self, p, no):
            r = None
            for n in p:
                if n.no == no:
                    r = n
                    return n
                else:
                    if len(n.childs.tasks) > 0:
                        r = find(self, n.childs.tasks, no)
                        if r != None:
                            return r

        r = None
        for t in self.tasks:
            if t.no == no:
                r = t
                return r
            else:
                if len(t.childs.tasks) > 0:
                    r = find(self, t.childs.tasks, no)
                    if r != None:
                        return r

    def clone(self):
        """克隆
        """

        def _clone(self, c):
            for t in c.childs.tasks:
                nt = t.clone()
                _clone(self, nt)

        tc = nodeTaskz()
        for t in self.tasks:
            nt = t.clone()
            tc.add(nt)
            _clone(self, nt)

        return tc

    '''
    打印
    '''

    def printer(self, type):
        def __toString(self, type, t):

            toStr = {
                stageType.LC.value: lambda: t.toStringLC(),
                stageType.LP.value: lambda: t.toStringLP()
            }

            return toStr[type.value]()

        def p(self, p, i, type):
            s = ''
            for t in p.childs.tasks:
                for j in range(i):
                    s += '\t'

                print(s + __toString(self, type, t))
                s = ''
                if len(t.childs.tasks) > 0:
                    p(self, t, i + 1)

        i = 0
        for t in self.tasks:
            print(__toString(self, type, t))
            if len(t.childs.tasks) > 0:
                p(self, t, i + 1, type)

