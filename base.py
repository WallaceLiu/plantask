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

    def initMatrix2(self, rn, cn):
        """初始化二维矩阵
        参数
            rn:     row number
            cn:     column number
        """
        m = []
        for i in range(rn):
            t = [0] * cn
            m.append(t)
        return m
