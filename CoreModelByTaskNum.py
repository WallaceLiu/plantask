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
                if self.map[r][i] == 1:
                    s.append(self.getTasksIndex()[i])
                    m(self, s, i)
                    s.pop()
                else:
                    if i >= self.getNodeNum() - 1:
                        p = '->'.join(s)
                        if self.__isPath(p) == False:
                            self.path.append(p)

        s = []
        for r in range(len(self.getRTask())):
            s.clear()
            if self.getRTask()[r] == 0:
                s.append(self.getTasksIndex()[r])
                m(self, s, r)

    def __isPath(self, path):
        """是否为一个任务路径
        """
        for p in self.getPath():
            if path == p:
                return True
        return False

    def __printer():
        pass

    def __estimate(self, s, w):
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


#    def model(self, minmax, weights, nodenum, plan, intervalMatrix):
#        """调优阶段
#        动态规划
#            
#            计算时间间隔内的任务数量
#
#        参数:
#            minmax:
#            weights:     时间间隔向量
#            nodenum:     任务节点数量       
#            plan:        任务评估时间最晚时间矩阵
#            intervalMatrix:
#                
#        返回:
#    
#        异常:
#            
#        """
#        r = []
#        s = []
#        #result=ModelBase.initResult(nodenum)
#
#        for i in range(len(weights)):
#            w = int(nodenum / (weights[i] - 1)) if weights[i] - 1 < 0 else 0
#            if w > 0:  # 只有一个时间间隔，无需优化
#                self.__model(self, minmax, w, nodenum, intervalMatrix[i], plan,
#                             r, s)
#
#        return r
#
#    def __model(self, minmax, w, nodenum, vector, plan, r, s):
#        """ 
#        
#        参数:
#            w:          权重
#            nodenum:    时间间隔向量
#            vector:     时间间隔向量
#            plan:       任务评估时间
#                     [{
#                'no': t.no,
#                'id': t.id,
#                'b': t.bDateTime,
#                'e': t.eDateTime,
#                'c': t.consume,
#                't': t.type
#            },...]
#            r:  结果
#            s:  堆栈
#            
#        返回:
#        异常:
#        """
#
#        def m(self, w, p, nodenum, vector, plan, r, s):
#            pass
#
##        i =0
##        s.append(plan[i][0])
##
##        while len(s)>0:
##            for r in range(nodenum):
##                if len(s)>=nodenum:
##                    if self.__target(s,w)<=w:
##                        r.append(s)
##                        s.pop()
##                    else:
##                        s.pop()
##                else:
##                    s.append()
#
#        for r in range(nodenum):
#            #s.append(plan[r][0])
#            print(plan[r][0])
#            m(self, plan[r][0], w, nodenum, vector, plan, r, s)
