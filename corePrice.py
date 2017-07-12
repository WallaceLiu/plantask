# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from base import base
from corePriceBase import corePriceBase


class corePrice(corePriceBase):
    def __init__(self, cm):
        corePriceBase.__init__(self, cm)

        print('-corePrice...')
        print('\t-Parameters Ready...')
        self.printParameters()

    def models(self):
        print('--Stage: corePrice.models...')

        for g in self.estimate.modelGraph:
            self.model(g)

        print('--corePrice.models End.')

    def model(self, g):
        """查找邻接矩阵所有路径
    
        参数:
        返回:
        异常:
        """

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

    def creatPriceMatrix():
        """创建代价矩阵
        二维矩阵
            [[-,-,-,-],[],[],...]
                其中，
                    [-,-,-,-]为[任务数量,CPU密集任务数量,IO密集任务数量,集群空闲时间]
        """
        pass