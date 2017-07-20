# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:15:48 2017

@author: liuning11
"""

from base import base
from nodeProjectz import nodeProjectz


class nodeProject(base):
    """
    """

    def __init__(self, no=0, id='0', realId='0', cproject=None):
        """构造函数
        """
        self.no = no
        self.id = id
        self.realId = realId
        self.cproject = cproject
        self.optional = nodeProjectz()

    def add(self, pro):
        """添加
        """
        self.optional.add(pro)

    def toString(self):
        s = '<' + str(self.no) + '>'
        s += ',' + str(self.id) + ',' + str(self.realId)
        s += ',' + (str(True) if self.cproject != None else str(False))
        return s

    def printer(self):
        cur = self
        no = 0

        while cur != None:
            s = ''
            for i in range(no):
                s += '\t'
            print(s + cur.toString())
            s += '\t'
            cur.optional.printer(s)
            cur = cur.cproject
            no = no + 1
