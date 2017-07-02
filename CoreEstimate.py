# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:23:23 2017

@author: liuning11
"""
import DateTimeUtil


class CoreEstimate:
    """评估阶段
    
    包括，
    1，计算所有任务最晚发生时间
    2，计算时间间隔序列矩阵
    3，计算时间间隔矩阵的平均任务数

    """

    steps = [600, 1200, 1800, 2400, 3000, 3600]
    timeSeq = []
    avgTasksNum = []
    plans = []

    def __init__(self, g):
        """构造函数

        参数:
            g: 图
                
        返回:
    
        异常:
        """
        self.graph = g

        self.__estimate()

    def __estimate(self):

        print('Estimate...')

        self.__computePlan()

        minmax = self.__getMinMax(self.graph.tasks.tasks)

        self.__createTimeSeq(self.steps, minmax, self.graph)

        self.__initAvgTasksNum(self.steps, minmax, self.graph)

        print('Estimate Complete.')

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
            for i in range(self.graph.nodenum):
                if m[i][r] == 1:
                    t = self.graph.findRootTask(self.graph.tasksIndex[i])

                    self.__deal(t, c.bDateTime - t.consume - 1,
                                c.bDateTime - 1, plan[i])

                    compute(self, i, t, m, plan)

        self.__initPlan()

        for i in range(self.graph.nodenum):
            if self.graph.tTask[i] == 0:
                c = self.graph.findRootTask(self.graph.tasksIndex[i])
                if c.bDateTime != None:
                    self.__deal(c, c.bDateTime, c.bDateTime + c.consume,
                                self.plans[i])

                    compute(self, i, c, self.graph.map, self.plans)

        self.__printPlan(True)

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
        """
        for i in range(self.graph.nodenum):
            self.plans.append([])

    def __getMinMax(self, tasks):
        """获得任务中最早最晚时间
        
            按开始时间排序
        
        参数:
        返回:
    
        异常:
            
        """
        tk = sorted(tasks, key=lambda x: x.bDateTime)
        minmax = (tk[0].bDateTime, tk[len(tk) - 1].bDateTime)

        print('Min And Max Task Time:', minmax)

        return minmax

    def __initAvgTasksNum(self, steps, minmax, g):
        """创建时间序列矩阵
            
            按开始时间排序
        
        参数:
            step:   步进时间，单位为秒
            g:      任务图
        返回:
    
        异常:
                
        """
        for step in steps:
            self.avgTasksNum.append(int((minmax[1] - minmax[0]) / step) + 1)

        print('Avg Task Number:')
        print(self.avgTasksNum)

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

        return meta

    def __createTimeSeq(self, steps, minmax, g):
        """创建时间序列矩阵
        
            按开始时间排序
        
        参数:
            step:   步进时间，单位为秒
            g:      任务图
        返回:
    
        异常:
            
        """

        def createTimeSeqVector(self, minmax, step):
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

        print('Time Seq Step:')
        print(steps)
        for s in self.steps:
            self.timeSeq.append(createTimeSeqVector(self, minmax, s))

        self.__printTimeSeq(True)

    def __printPlan(self, isReadable):
        """打印评估时间
        """
        print('Last Time When Occur:')
        for r in self.plans:
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

    def __printTimeSeq(self, isReadable):
        """打印时间矩阵
        """
        print('Time Seq Matrix:')
        for r in self.timeSeq:
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
