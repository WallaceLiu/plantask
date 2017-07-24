# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:23:23 2017

@author: liuning11
"""
import datetimeUtil
from coreBase import coreBase


class nodeAdjMatrixEs(coreBase):
    """评估阶段
    
    包括，
    1，计算所有任务最晚发生时间
    
    参数:
        __plans:    根据终端任务节点计算的每个任务的最晚开始时间

    """

    __plans = []

    def __init__(self, g):
        """构造函数

        参数:
            g: 图
                
        返回:
    
        异常:
        """

        self.__estimate(g)

    def __estimate(self, g):
        """设置所有任务的最晚时间
        """

        def init(self, g):
            """初始化评估
            """
            for i in range(g.nodenum):
                self.__plans.append([])

        def compute(self, r, c, g, plan):
            """计算所有任务的最晚时间
    
            参数:
                r:      节点索引
                c:      节点
                m:      邻接矩阵
                plan:   评估时间
                    
            返回:
        
            异常:
                
            """
            for i in range(g.nodenum):
                if g.map[i][r] > 0:
                    t = g.findRootTask(g.tasksIndex[i])

                    self.__deal(t, c.bDateTime - t.consume - 1,
                                c.bDateTime - 1, plan[i])

                    compute(self, i, t, g, plan)

        init(self, g)

        for i in range(g.nodenum):
            if g.tTask[i] == 0:
                c = g.findRootTask(g.tasksIndex[i])
                if c.bDateTime != None:
                    self.__deal(c, c.bDateTime, c.bDateTime + c.consume,
                                self.__plans[i])

                    compute(self, i, c, g, self.__plans)

        print('--Stage: nodeAdjMatrixEs.__estimate...')
        if self.config.debug == True:
            self.__printer(True)

        print('--nodeAdjMatrixEs.__estimate End.')

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

    """
    打印
    """

    def __printer(self, isReadable):
        """打印评估时间
        """
        for r in self.__plans:
            l = []
            for c in r:
                if isReadable:
                    l.append('(' + str(c.get('no')) + ',' + str(c.get(
                        'id')) + ',' + datetimeUtil.timestamp_datetime(
                            c.get('b')) + ',' +
                             datetimeUtil.timestamp_datetime(c.get('e')) + ','
                             + str(c.get('c')) + ',' + str(c.get('t')) + ')')
                else:
                    l.append(c)

            print(l)
