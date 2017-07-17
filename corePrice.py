# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from corePriceBase import corePriceBase


class corePrice(corePriceBase):
    def __init__(self, cm, g):
        corePriceBase.__init__(self, cm, g)

        print('\t-Parameters Ready...')
        self.printParameters()

    def model(self, g):
        """查找邻接矩阵所有路径
    
        参数:
        返回:
        异常:
        """
        print('--Stage: corePrice.model...')
        print('--corePrice.model End.')
        pass

    def price(self, g, path, avgTask):
        """目标函数
        
        计算堆栈中所有节点的目标值
        
        参数:
            s:          权重
            r:    时间间隔向量
            
        返回:
        异常:
        """
        pass
