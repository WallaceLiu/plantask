# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:15:48 2017

@author: liuning11
"""

from base import base
from nodeProjectz import nodeProjectz


class nodeProject(base):
    """邻接矩阵
    """

    __no = None
    __id = None
    __realId = None
    __optional = nodeProjectz()
    __cproject = None

    def __init__(self, no=0, id='', realId=''):
        """构造函数
        """
        self.__id = id
        self.__realId = realId

    def add(self, pro):
        """添加
        """
        self.__optional.add(pro)

    def toString(self):
        pass
