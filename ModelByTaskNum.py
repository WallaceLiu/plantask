# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from ModelBase import ModelBase
import random

class ModelByTaskNum(ModelBase):
    def __init__(self, g):
        ModelBase.__init__(self, g)

    def model(self):
        """计算所有任务的最晚时间

        """
        def m(self, r, c, m, plan):
            """计算所有任务的最晚时间
    
            参数:
                r:      节点索引
                c:      节点
                m:      邻接矩阵
                plan:   评估时间
                    
            返回:
        
            异常:
                
            """
            for i in range(self._graph.nodenum):
                if m[i][r] == 1:
                    t = self._graph.findRootTask(self._graph.tasksIndex[i])

                    self.__deal(t, c.bDateTime - t.consume - 1,
                                c.bDateTime - 1, plan[i])

                    m(self, i, t, m, plan)

        self.__initPlan()

        for i in range(self._graph.nodenum):
            if self._graph.tTask[i] == 0:
                c = self._graph.findRootTask(self._graph.tasksIndex[i])
                if c.bDateTime != None:
                    self.__deal(c, c.bDateTime, c.bDateTime + c.consume,
                                self._estimate[i])

                    m(self, i, c, self._graph.map, self._plan)

        self.__printer()

    def __deal(self, t, bDt, eDt, pl):
        """计算任务最晚时间

        参数:
            t:      任务
            bDt:    开始时间
            eDt:    结束时间
            pl:     最晚时间
            
        返回:
    
        异常:
        """

        def setTask(self, t, bDt, eDt):
            if t.bDateTime == None:
                t.bDateTime = bDt
                t.eDateTime = eDt
            else:
                if t.bDateTime < bDt:
                    t.bDateTime = bDt
                    t.eDateTime = eDt
                    pl.clear()

        def addPlan(self, pl, p):
            if len(pl) <= 0:
                pl.append(p)
            else:
                if pl[0].get('b') <= p.get('b'):
                    pl.clear()
                    pl.append(p)

        setTask(self, t, bDt, eDt)

        addPlan(self, pl, {
            'no': t.no,
            'id': t.id,
            'b': t.bDateTime,
            'e': t.eDateTime,
            'c': t.consume,
            't': t.type
        })

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

    def __random(self, step):
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
