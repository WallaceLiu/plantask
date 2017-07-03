# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from CoreModelBase import CoreModelBase
import random


class CoreModelByTaskNum(CoreModelBase):
    def __init__(self, e):
        CoreModelBase.__init__(self, e)

    def model(self):
        """查找邻接矩阵所有路径
    
        参数:
        返回:
        异常:
        """

        def m(self, s, r):
            for i in range(self.getNodeNum()):
                if self.getMap()[r][i] == 1:
                    s.append(self.getTasksIndex()[i])
                    m(self, s, i)
                    s.pop()
                else:
                    if i >= self.getNodeNum() - 1:
                        p = '->'.join(s)
                        if self.__isPath(p) == False:
                            self.path.append(p)

        print('--Model Stage...')
        s = []
        for r in range(self.getNodeNum()):
            s.clear()
            if self.getRTask()[r] == 0:
                s.append(self.getTasksIndex()[r])
                m(self, s, r)

        print('--Model Stage Complete.')
        print(self.path)

    def __isPath(self, path):
        """是否为一个任务路径
        """
        for p in self.getPath():
            if path == p:
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


