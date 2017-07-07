# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:23:23 2017

@author: liuning11
"""
import DateTimeUtil
from base import base
from TaskCollection import TaskCollection


class CoreEstimate(base):
    """评估阶段
    
    包括，
    1，计算所有任务最晚发生时间
    2，计算时间间隔序列矩阵
    3，计算时间间隔矩阵的平均任务数
    
    
    参数:
        steps:          时间间隔，单位秒
        period:         周期，单位小时，默认为24小时
        timeSeq:        弃用
        stepsNum:    理论上，每个时间间隔内的平均任务数量
        plans:          根据终端任务节点计算的每个任务的最晚开始时间

    """

    steps = [600]
    period = 1
    minmax = None
    stepsNum = []
    plans = []
    timeSeq = []
    modelGraph = []

    def __init__(self, g):
        """构造函数

        参数:
            g: 图
                
        返回:
    
        异常:
        """

        self.__estimate(g)

        self.__createModelGraph(g)

    def __createModelGraph(self, g):
        """
        任务关系：
        a->b->c
        a->b->d->e
        f->e
        
        每个任务都持续10分钟，任务e为9点30分钟开始
        
        那么，最早最晚的时间：<2017-06-25 08:30:00,2017-06-25 09:30:00>
        其中，时间“2017-06-25 09:30:00”是最晚执行的一个任务，
        如果设置周期为1小时，则最早的时间为“2017-06-25 08:30:00”
        
        
        
        <12>	10:12	10	a
        		运行时间(2017-06-25 08:49:58,2017-06-25 08:59:58,600)	运行阈值(-,-)
        <13>	10:13	10	a
        		运行时间(2017-06-25 08:39:58,2017-06-25 08:49:58,600)	运行阈值(-,-)
        <14>	20:14	20	b
        		运行时间(2017-06-25 08:59:59,2017-06-25 09:09:59,600)	运行阈值(-,-)
        <15>	20:15	20	b
        		运行时间(2017-06-25 08:49:59,2017-06-25 08:59:59,600)	运行阈值(-,-)
        <16>	20:16	20	b
        		运行时间(2017-06-25 08:39:59,2017-06-25 08:49:59,600)	运行阈值(-,-)
        <17>	40:17	40	d
        		运行时间(2017-06-25 09:09:59,2017-06-25 09:19:59,600)	运行阈值(-,-)
        <18>	40:18	40	d
        		运行时间(2017-06-25 08:59:59,2017-06-25 09:09:59,600)	运行阈值(-,-)
        <19>	40:19	40	d
        		运行时间(2017-06-25 08:49:59,2017-06-25 08:59:59,600)	运行阈值(-,-)
        <20>	40:20	40	d
        		运行时间(2017-06-25 08:39:59,2017-06-25 08:49:59,600)	运行阈值(-,-)
        <21>	60:21	60	f
        		运行时间(2017-06-25 09:09:59,2017-06-25 09:19:59,600)	运行阈值(-,-)
        <22>	60:22	60	f
        		运行时间(2017-06-25 08:59:59,2017-06-25 09:09:59,600)	运行阈值(-,-)
        <23>	60:23	60	f
        		运行时间(2017-06-25 08:49:59,2017-06-25 08:59:59,600)	运行阈值(-,-)
        <24>	60:24	60	f
        		运行时间(2017-06-25 08:39:59,2017-06-25 08:49:59,600)	运行阈值(-,-)
        
        
        ['10', '20', '30', '40', '50', '60', 
        '10:12', '20:14', '10:13', '20:15', '40:17', 
        '40:18', '20:16', '40:19', '40:20', 
        '60:21', '60:22', '60:23', '60:24']
        
        
                a   b  c  d  e  f   12 14 13 15 17 18 16 19 20 21 22 23 24
            a   [0, 1, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            b   [0, 0, 1, 1, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            c   [0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            d   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            e   [0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            f   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
        10:12   [0, 0, 0, 0, 0, 0,  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        20:14   [0, 0, 1, 0, 0, 0,  0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        10:13   [0, 0, 0, 0, 0, 0,  0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        20:15   [0, 0, 1, 0, 0, 0,  0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        40:17   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        40:18   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        20:16   [0, 0, 1, 0, 0, 0,  0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
        40:19   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        40:20   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        60:21   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        60:22   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        60:23   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        60:24   [0, 0, 0, 0, 1, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        
        """

        def ready(self, g, step, minmax):
            no = g.edgenum + g.nodenum + 1
            arr = []
            for i in range(g.nodenum):
                if g.tTask[i] == 1:
                    t = g.findRootTask(g.tasksIndex[i])
                    bDt = t.bDateTime - step
                    while bDt >= self.minmax[0]:
                        nt = t.cloneLocal()
                        nt.no = no
                        nt.id = nt.id + ':' + str(no)  # 新ID=原ID+序号
                        nt.bDateTime = bDt
                        nt.eDateTime = nt.bDateTime + nt.consume

                        arr.append(nt)

                        bDt = bDt - step
                        no = no + 1

            #if base.config.debug == True:
            print('Optional Task:')
            for a in arr:
                print(a.toString(True))

            return arr

        def create(self, g, step, minmax):
            """创建模型使用的任务图
            """
            t_arrs = ready(self, g, step, minmax)

            ng = g.clone()

            no = t_arrs[len(t_arrs) - 1].no + 1

            for t_arr in t_arrs:  # 添加节点
                n = t_arr.cloneLocal()
                ng.add(ng.tasks, n)
                no = no + 1

                node = ng.findRootTask(t_arr.realId)

                for c in node.childs.tasks:  # 添加节点边
                    t = ng.findRootTask(c.realId)

                    if len(t.childs.tasks) == 0:
                        ng.add(n.childs, t.cloneLocal())  # 添加终端节点的边
                    else:
                        edges = filter(
                            lambda x: t.realId == x.realId and t_arr.eDateTime <= x.bDateTime,
                            t_arrs)

                        for edge in edges:
                            e = edge.cloneLocal()
                            ng.add(n.childs, e)

            ng.createMap()
            ng.printGraph()

            return ng

        print('--Stage Model Graph...')

        if self.config.debug == True:
            print('\t-Min and Max:<%s,%s>' %
                  (DateTimeUtil.timestamp_datetime(self.minmax[0]),
                   DateTimeUtil.timestamp_datetime(self.minmax[1])))

        self.modelGraph.clear()

        for step in self.steps:
            self.modelGraph.append(create(self, g, step, self.minmax))

        print('--Model Graph Complete.')

        return self.modelGraph

    def __estimate(self, g):

        print('--Stage Estimate...')

        self.minmax = self.__getMinMax(g.lastOccurTime)

        self.__computePlan(g)

        #self.createTimeSeq(self.steps, minmax, self.graph)

        self.__initStepsNum(self.steps, self.minmax, g)

        print('--Estimate Complete.')

    def __computePlan(self, g):
        """计算所有任务的最晚时间
        """

        def init(self, g):
            """初始化评估矩阵
            """
            for i in range(g.nodenum):
                self.plans.append([])

        def compute(self, r, c, m, plan, g):
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
                if m[i][r] == 1:
                    t = g.findRootTask(g.tasksIndex[i])

                    self.__deal(t, c.bDateTime - t.consume - 1,
                                c.bDateTime - 1, plan[i])

                    compute(self, i, t, m, plan, g)

        init(self, g)

        for i in range(g.nodenum):
            if g.tTask[i] == 0:
                c = g.findRootTask(g.tasksIndex[i])
                if c.bDateTime != None:
                    self.__deal(c, c.bDateTime, c.bDateTime + c.consume,
                                self.plans[i])

                    compute(self, i, c, g.map, self.plans, g)

        if self.config.debug == True:
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

    def __getMinMax(self, lastOccurTime):
        """获得任务中最早最晚时间
        """
        minmax = (lastOccurTime - self.period * 3600, lastOccurTime)

        if self.config.debug == True:
            print('\t-Min And Max Task Time:', minmax)

        return minmax

    def sortBDateTime(self, tasks):
        return sorted(tasks, key=lambda x: x.bDateTime)

    def __initStepsNum(self, steps, minmax, g):
        """初始化时间间隔数量
            
            按开始时间排序
        
        参数:
            step:   步进时间，单位为秒
            g:      任务图
        返回:
    
        异常:
                
        """
        for step in steps:
            self.stepsNum.append(int(self.period * 3600 / step) + 1)

        if self.config.debug == True:
            print('\t-Interval Number in Steps:')
            print(self.stepsNum)

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

    def createTimeSeq(self, steps, minmax, g):
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

        for s in self.steps:
            self.timeSeq.append(createTimeSeqVector(self, minmax, s))

        if self.config.debug == True:
            print('\t-Time Seq Step:')
            print(steps)
            self.__printTimeSeq(True)

        return self.timeSeq

    def __printPlan(self, isReadable):
        """打印评估时间
        """
        print('\t-Last Time When Every Task Occur:')
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
        print('\t-Time Seq Matrix:')
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

    def printModelGraph(self):
        for g in self.modelGraph:
            print(g.printTasks())
