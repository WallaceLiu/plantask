# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from coreModelBase import coreModelBase
import random


class coreModelByTaskNum(coreModelBase):
    def __init__(self, e):
        coreModelBase.__init__(self, e)

    def models(self):
        print('--Stage: CoreModelByTaskNum.models...')

        for g in self.estimate.modelGraph:
            self.model(g)

        print('--CoreModelByTaskNum.models End.')

    def model(self, g):
        """查找邻接矩阵所有路径
    
        参数:
        返回:
        异常:
        """

        def m(self, s, r):
            for i in range(g.nodenum):
                if g.map[r][i] > 0:
                    s.append(g.tasksIndex[i])
                    m(self, s, i)
                    s.pop()
                else:
                    if i >= g.nodenum - 1:
                        p = '->'.join(s)
                        if self.__isPath(p) == False :
                            self.path.append(p)

        s = []
        for r in range(g.nodenum):
            s.clear()
            if g.rTask[r] == 0:
                s.append(g.tasksIndex[r])
                m(self, s, r)

        print(self.path)

    def __isPath(self, path):
        """是否为一个任务路径
        """
        for p in self.path:
            if path in p:
                return True
        return False

    def __printer():
        pass

    def __price(self, s, w):
        """目标函数
        
        计算堆栈中所有节点的目标值
        
        参数:
            s:          权重
            r:    时间间隔向量
            
        返回:
        异常:
        """
        if len(s) <= 0:
            return 0

        t = w
        return t

    def __moving(self, step):
        """随机时间
            避免在移动任务时，都聚集在一个时间点
            
        参数:
            step:   时间间隔
                
        返回:
            随机时间
            
        异常:
        """
        seed = random.randint(0, 100)
        return int(step * (1 + seed / 100))
