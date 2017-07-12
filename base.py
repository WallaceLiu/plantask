# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:02:25 2017

@author: liuning11
"""
from config import config


class base:
    config = config()

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
