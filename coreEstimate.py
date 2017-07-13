# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:23:23 2017

@author: liuning11
"""
import datetimeUtil
from coreBase import coreBase
import random
from nodeAdjMatrix import nodeAdjMatrix


class coreEstimate(coreBase):
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

    minmax = None
    modelGraph = nodeAdjMatrix()
    plans = []

    def __init__(self, g):
        """构造函数

        参数:
            g: 图
                
        返回:
    
        异常:
        """

        self.__estimate(g)

        self.__createModelGraph(g, self.minmax)

    def __estimate(self, g):

        print('--Stage: CoreEstimate.__estimate...')

        self.minmax = self.__getMinMax(g.lastOccurTime)

        self.__computePlan(g)

        print('--CoreEstimate.__estimate End.')

    def __computePlan(self, g):
        """设置所有任务的最晚时间
        """

        def init(self, g):
            """初始化评估
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
                if m[i][r] > 0:
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
        minmax = (lastOccurTime - self.config.period * 3600, lastOccurTime)

        if self.config.debug == True:
            print('\t-CoreEstimate.__getMinMax:', minmax)

        return minmax

    """
    core 
    """

    def __createModelGraph(self, g, minmax):
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
        
        
        - 指定节点的子节点，看行，如行b，有两个大于0的值，c和d，即为其子节点
        - 指定节点的父节点，看列，如列b，有一个大于0的值，a，即为其父节点
        
 
    
        ['10', '20', '30', '40', '50', '60', 
        '10:12', '20:14', '10:13', '20:15', 
        '40:16', '40:17', '40:18', '60:19', 
        '60:20', '60:21', '60:22']
        
                a   b    c   d   e   f   12  14  13  15  16  17 18  19 20 21 22 
            a   [0, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
            b   [0,  0, 10, 10,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
            c   [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
            d   [0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
            e   [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
            f   [0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
            
        10:12   [0,  0,  0,  0,  0,  0,  0, 10,  0,  0,  0,  0, 0,  0, 0, 0, 0]
        20:14   [0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 10,  0, 0,  0, 0, 0, 0]
        10:13   [0,  0,  0,  0,  0,  0,  0, 10,  0, 10,  0,  0, 0,  0, 0, 0, 0]
        20:15   [0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 10, 10, 0,  0, 0, 0, 0]
        40:16   [0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
        40:17   [0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
        40:18   [0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
        60:19   [0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
        60:20   [0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
        60:21   [0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
        60:22   [0,  0,  0,  0, 10,  0,  0,  0,  0,  0,  0,  0, 0,  0, 0, 0, 0]
        
        
    上面可以看到，x_16*16，即b，是不合理的，没有任何父节点~   
        
        """

        def ready(self, g, step, minmax):

            if self.config.debug == True:
                print('\t-CoreEstimate.__createModelGraph.ready...')
                print('\t\t-Min and Max:<%s,%s>' %
                      (datetimeUtil.timestamp_datetime(minmax[0]),
                       datetimeUtil.timestamp_datetime(minmax[1])))

            no = g.edgenum + g.nodenum + 1
            arr = []
            for i in range(g.nodenum):
                if g.tTask[i] == 1:  # 非终端任务节点
                    t = g.findRootTask(g.tasksIndex[i])
                    bDt = t.bDateTime - step
                    win = maxParentConsume(self, g.map, g.nodenum, i)

                    if self.config.debug == True:
                        print(
                            '\t\t-ready:%s      win=%s      end=%s    step=%s'
                            %
                            (t.id, win,
                             datetimeUtil.timestamp_datetime(minmax[0] + win),
                             str(step)))

                    while bDt > minmax[0] + win:
                        nt = t.cloneLocal()
                        nt.no = no
                        nt.id = nt.id + ':' + str(no)  # 新ID=原ID+序号
                        nt.bDateTime = bDt
                        nt.eDateTime = nt.bDateTime + nt.consume

                        arr.append(nt)

                        if self.config.debug == True:
                            print('\t\t\t-Add New:%s' % nt.toStringTime())

                        bDt = bDt - step
                        no = no + 1

            if coreBase.config.debug == True:
                print('\t-CoreEstimate.__createModelGraph.ready:')
                for a in arr:
                    print(a.toString(True))

            return arr

        def maxParentConsume(self, matrix, nodenum, c):
            m = 0
            r = c
            consume = 0
            while r >= 0:
                rt = -1
                for i in range(nodenum):
                    if matrix[i][r] > m:
                        m = matrix[i][r]
                        rt = i
                if rt > 0:
                    consume += m
                r = rt

            return consume

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

            #ng.printGraph()

            return ng

        print('--Stage: CoreEstimate.__createModelGraph...')

        self.modelGraph = create(self, g, self.config.timeStep, minmax)

        print('--CoreEstimate.__createModelGraph End.')

        return self.modelGraph

    def sortBDateTime(self, tasks):
        return sorted(tasks, key=lambda x: x.bDateTime)

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

    """
    打印
    """

    def __printPlan(self, isReadable):
        """打印评估时间
        """
        print('\t-Last Time When Every Task Occur:')
        for r in self.plans:
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

    def printModelGraph(self):
        for g in self.modelGraph:
            print(g.printTasks())
