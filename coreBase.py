# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:23:23 2017

@author: liuning11
"""
from base import base


class coreBase(base):
    def __init__(self):
        pass

    def initMatrix2(self, v, rn, cn):
        """初始化二维矩阵
        参数
            rn:     row number
            cn:     column number
        """
        m = []
        for i in range(rn):
            t = [v] * cn
            m.append(t)
        return m

    def initVector(v, n):
        """初始化向量
        参数
            n:     row number
        """
        return [v] * n
