# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:23:23 2017

@author: liuning11
"""
from TaskAdjMatrix import TaskAdjMatrix
import DateTimeUtil


class Plan:
    """时间规划
    
    分两个阶段：
    1，评估阶段
        任务分为两种：
        a，关键任务，该任务根据业务要求必须设置结束时间，并且在调优阶段不能改变
        b，非关键任务，该任务给出的时间，可以改变
        在整个任务的图结构中，至少给出一个任务的结束时间，规划才能开始
        
        评估图中每个任务的父任务和子任务的时间，这样，每个任务都会有时间，从中选择最早的时间
        
    2，调优阶段
        1·）保证每个时间段的任务数量差不多
        2）并在此基础上，保证任务类型的数量差不多
            任务至少具备两种类型：
            a，CPU密集型
            b，IO密集型
    """

    def __init__(self, g):
        """构造函数

        参数:
            g: 图
                
        返回:
    
        异常:
        """
        self._graph = g
        self._IntervalMatrix = []
        self._steps = [600, 1200, 1800, 2400, 3000, 3600]
        self._plan = []

    def estimate(self):
        """评估阶段

        参数:
                
        返回:
    
        异常:
        """
        self.__computePlan()

        self.__createIntervalMatrix(self._steps, self._graph)

        self.__tuning()

    def __tuning(self):
        """调优阶段
        计算时间间隔内的任务数量
        根据每个时间段的任务数量调优
        根据每个时间段的任务类型调优

        参数:
                
        返回:
    
        异常:
            
        """
        pass

    def __computePlan(self):
        """计算所有任务的最晚时间

        参数:
                
        返回:
    
        异常:
            
        """

        def compute(self, r, c, m, plan):
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

                    self.__setTask(t, c.bDateTime - t.consume - 1,
                                   c.bDateTime - 1)
                    self.__addPlan(plan[i], {
                        'b': t.bDateTime,
                        'e': t.eDateTime,
                        'c': t.consume,
                        't': t.type
                    })

                    compute(self, i, t, m, plan)

        self.__initPlan()

        for i in range(self._graph.nodenum):
            if self._graph.tTask[i] == 0:
                c = self._graph.findRootTask(self._graph.tasksIndex[i])
                if c.bDateTime != None:
                    self.__addPlan(self._plan[i], {
                        'b': c.bDateTime,
                        'e': c.bDateTime + c.consume,
                        'c': c.consume,
                        't': c.type
                    })

                    compute(self, i, c, self._graph.map, self._plan)

        self.__printPlan(True)

    def __addPlan(self, pl, p):
        """添加评估时间
        
        取最晚的时间

        参数:
            pl: 评估时间
            p: 新估计时间
                
        返回:
    
        异常:
            
        """
        if len(pl) <= 0:
            pl.append(p)
        else:
            if pl[0].get('b') <= p.get('b'):
                pl.clear()
                pl.append(p)

    def __setTask(self, t, bDt, eDt):
        if t.bDateTime == None:
            t.bDateTime = bDt
            t.eDateTime = eDt
        else:
            if t.bDateTime < bDt:
                t.bDateTime = bDt
                t.eDateTime = eDt

    def __initPlan(self):
        """初始化评估矩阵

        参数:
                
        返回:
    
        异常:
            
        """
        for i in range(self._graph.nodenum):
            self._plan.append([])

    def __getMinMax(self, tasks):
        """获得任务中最早最晚时间
        
            按开始时间排序
        
        参数:
        返回:
    
        异常:
            
        """
        tk = sorted(tasks, key=lambda x: x.bDateTime)
        l = len(tk)
        return (tk[0].bDateTime, tk[l - 1].bDateTime)

    def __createIntervalMatrix(self, steps, g):
        """创建时间序列矩阵
        
            按开始时间排序
        
        参数:
            step:   步进时间，单位为秒
            g:      任务图
        返回:
    
        异常:
            
        """
        print('时间步长：')
        print(steps)
        minmax = self.__getMinMax(g.tasks.tasks)
        print('任务最早/最晚时间：')
        print(minmax)
        
        for s in steps:
            self._IntervalMatrix.append(self.__createIntervalVector(minmax, s))

        print('时间间隔序列：')
        self.__printIntervalMatrix(True)

    def __createIntervalVector(self, minmax, step):
        """创建时间序列向量

        参数:
            minmax: 最小最大日期.
            step:步长,单位为秒.
                
        返回:
            {'bt': b, 'et': e, 'na': 0, 'nk': 0, 'ng': 0}
            
            bt - 开始时间
            et - 结束时间
            na - 任务数量
            nk - 关键任务数量
            ng - 非关键任务数量
    
        异常:
            
        """
        mm = self.__minmaxMoving(minmax, step)
        v = []
        b = mm[0]
        e = None
        while b < mm[1]:
            e = b + step
            v.append({'bdt': b, 'edt': e, 'na': 0, 'nk': 0, 'ng': 0})
            b = e + 1
        return v

    def __minmaxMoving(self, minmax, step):
        """平移时间-折半平移，便于任务落在哪个时间段

        参数:
            minmax:最早最晚时间
            step:步长,单位为秒
                
        返回:
            (最早时间, 最晚时间)
            
        异常:
            
        """
        v = int(step / 2)
        return (minmax[0] - v, minmax[1] + v)

    def __random(self,step):
        pass
    '''
    打印
    '''

    def __printIntervalMatrix(self, isReadable):
        """打印时间矩阵
            
        """
        for r in self._IntervalMatrix:
            l = []
            for c in r:
                if isReadable:
                    l.append('(' + DateTimeUtil.timestamp_datetime(
                        c.get('bdt')) + ',' + DateTimeUtil.timestamp_datetime(
                            c.get('edt')) + ',' + str(c.get('na')) + ',' + str(
                                c.get('nk')) + ',' + str(c.get('ng')) + ')')
                else:
                    l.append(c)

            print(l)

    def __printPlan(self, isReadable):
        """打印评估时间
            
        """
        print('评估结果：')
        for r in self._plan:
            l = []
            for c in r:
                if isReadable:
                    l.append('(' + DateTimeUtil.timestamp_datetime(
                        c.get('b')) + ',' + DateTimeUtil.timestamp_datetime(
                            c.get('e')) + ',' + str(c.get('c')) + ',' + str(
                                c.get('t')) + ')')
                else:
                    l.append(c)

            print(l)
