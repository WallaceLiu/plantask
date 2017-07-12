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

    __id = None
    __realId = None
    __projects = nodeProjectz()

    def __init__(self):
        """构造函数
        """
