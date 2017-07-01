# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:42:10 2017

@author: liuning11
"""


class ModelBase:
    def __init__(self, g):
        self._graph = g
        self._plan = []

        self.__initPlan()

    def __initPlan(self):
        """初始化评估矩阵
        """
        for i in range(self._graph.nodenum):
            self._plan.append([])
            
    def model(self, weights, nodenum, plan, intervalMatrix):
        pass

    def initResult(self, nodenum):
        result = []
        for i in range(nodenum):
            result.append([])

        return result
