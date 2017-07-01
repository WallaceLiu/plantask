# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:23:23 2017

@author: liuning11
"""
from TaskAdjMatrix import TaskAdjMatrix
import DateTimeUtil
import random
from ModelBase import ModelBase


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

    def __init__(self, g, model=None):
        """构造函数

        参数:
            g: 图
                
        返回:
    
        异常:
        """
        self._graph = g
        self._steps = [600, 1200, 1800, 2400, 3000, 3600]
        self._weights = []
        self._intervalMatrix = []
        self._plan = []
        self._model = ModelBase()

    def estimate(self):
        """评估阶段

        """
        self.__computePlan()

        self.__createMatrix(self._steps, self._graph)

        self.__initWeight(self._steps, self._graph)

        self.__model(self._weights, self._graph.nodenum, self._plan,
                     self._intervalMatrix)

    def __computePlan(self):
        """计算所有任务的最晚时间

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

                    self.__deal(t, c.bDateTime - t.consume - 1,
                                c.bDateTime - 1, plan[i])

                    compute(self, i, t, m, plan)

        self.__initPlan()

        for i in range(self._graph.nodenum):
            if self._graph.tTask[i] == 0:
                c = self._graph.findRootTask(self._graph.tasksIndex[i])
                if c.bDateTime != None:
                    self.__deal(c, c.bDateTime, c.bDateTime + c.consume,
                                self._plan[i])

                    compute(self, i, c, self._graph.map, self._plan)

        self.__printPlan(True)

    def __model(self, weights, nodenum, plan, intervalMatrix):
        """调优阶段
            动态规划
        参数:
            weights:     时间间隔向量
            nodenum:     任务节点数量       
            plan:        任务评估时间最晚时间矩阵
                
        返回:
    
        异常:
            
        """
        return self._model.model(weights, nodenum, plan, intervalMatrix)

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
        minmax = (tk[0].bDateTime, tk[len(tk) - 1].bDateTime)

        print('任务最早/最晚时间：')
        print(minmax)

        return minmax

    def __initWeight(self, steps, g):
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

        for step in steps:
            self._weights.append(int((minmax[1] - minmax[0]) / step) + 1)

        print('时间间隔序列长度：')
        print(self._weights)

    def __minmaxMoving(self, minmax, step):
        """平移时间-折半平移，便于任务落在哪个时间段

        参数:
            minmax:     最早最晚时间
            step:       步长,单位为秒
                
        返回:
            (最早时间, 最晚时间)
            
        异常:
            
        """
        v = int(step / 2)
        meta = (minmax[0] - v, minmax[1] + v)

        print('任务最早/最晚时间-平移后：')
        print(meta)

        return meta

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

    def __createMatrix(self, steps, g):
        """创建时间序列矩阵
        
            按开始时间排序
        
        参数:
            step:   步进时间，单位为秒
            g:      任务图
        返回:
    
        异常:
            
        """

        def createVector(self, minmax, step):
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

        print('时间步长：')
        print(steps)
        minmax = self.__getMinMax(g.tasks.tasks)
        for s in self._steps:
            self._intervalMatrix.append(createVector(self, minmax, s))

        self._printIntervalMatrix(True)

    '''
    打印
    '''

    def _printIntervalMatrix(self, isReadable):
        """打印时间矩阵
        """
        print('时间间隔矩阵：')
        for r in self._intervalMatrix:
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
                    l.append('(' + str(c.get('no')) + ',' + str(c.get(
                        'id')) + ',' + DateTimeUtil.timestamp_datetime(
                            c.get('b')) + ',' +
                             DateTimeUtil.timestamp_datetime(c.get('e')) + ','
                             + str(c.get('c')) + ',' + str(c.get('t')) + ')')
                else:
                    l.append(c)

            print(l)
