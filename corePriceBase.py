# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from coreBase import coreBase
import datetimeUtil
from nodeProjectz import nodeProjectz
import re
from nodeProject import nodeProject


class corePriceBase(coreBase):

    __regx = ':\d+'
    __minmax = None
    __stepNum = []
    __originalPath = []
    __path = []
    __modelGraph = []
    __timeSeq = []
    __priceMatrix = []
    __projects = nodeProject()

    def __init__(self, cm, g):
        self.__minmax = cm.estimate.minmax
        self.__originalPath = g.path
        self.__path = cm.path
        self.__modelGraph = cm.estimate.modelGraph

        self.__initStepNum(self.config.timeStep, self.config.period)
        self.__initTimeSeq(self.config.timeStep, self.__minmax)

        self.__priceMatrix = self.initMatrix2(0, len(self.__timeSeq), 4)

        self.__createProjects(self.__path, self.__modelGraph.tasks)

    def price():
        """代价计算
        """
        pass

    def __createProjects(self, paths, tasks):
        pMatrix = self.__transform(paths)

        no = 0
        cur = self.__projects
        for p in paths:

            ts = filter(lambda x: x[1] == p, pMatrix)
            for t in ts:
                no = no + 1
                cur.add(nodeProject(no, t[0], t[1]))
            no = no + 1
            pro = nodeProject(no, '', '')
            cur = pro

    def __transform(self, paths):
        p = self.initMatrix2('', len(paths), 2)
        for i in range(len(p)):
            p[i][0] = paths[i]
            p[i][1] = re.sub(self.__regx, '', paths[i], count=0)
        return p

    def printParameters(self):
        print('\t\t-coreNewAdjMatrix.estimate.minmax:')
        print('(%s, %s)' % (
            (datetimeUtil.timestamp_datetime(self.__minmax[0]),
             datetimeUtil.timestamp_datetime(self.__minmax[1]))))
        print('\t\t-coreNewAdjMatrix.estimate.steps:')
        print(self.config.timeStep)
        print('\t\t-coreNewAdjMatrix.estimate.period:')
        print(self.config.period)
        print('\t\t-corePrice.stepNum:')
        print(self.__stepNum)
        print('\t\t-coreNewAdjMatrix.path:')
        print(self.__path)
        print('\t\t-coreNewAdjMatrix.estimate.modelGraph:')
        #print(self.__modelGraph[0].printGraph())
        #self.__printTimeSeq(True)
        #print(self.__priceMatrix)
        #print(self.__originalPath)
        self.printProjects()

    def __initStepNum(self, step, period):
        """初始化时间间隔数量
                
            按开始时间排序
        
        参数:
            step:   步进时间，单位为秒
            g:      任务图
        返回:
    
        异常:
                
        """
        self.__stepNum.append(int(period * 3600 / step) + 1)

        if self.config.debug == True:
            print('\t-corePrice.__initStepNum:')
            print(self.__stepNum)

    def __initTimeSeq(self, step, minmax):
        """创建时间序列矩阵
            
            按开始时间排序
        
        参数:
            step:   步进时间，单位为秒
            g:      任务图
        返回:
    
        异常:
            
        """

        def minmaxMoving(self, minmax, step):
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

        def createTimeSeqVector(self, minmax, step):
            """创建时间序列向量
        
            参数:
                minmax: 最小最大日期.
                step:步长,单位为秒.
                    
            返回:
                {'bt': b, 'et': e}
                
                bt - 开始时间
                et - 结束时间
        
            异常:
                
            """
            mm = minmaxMoving(self, minmax, step)
            v = []
            b = mm[0]
            e = None
            while b < mm[1]:
                e = b + step
                v.append({'bdt': b, 'edt': e})
                b = e + 1
            return v

        self.__timeSeq.append(createTimeSeqVector(self, minmax, step))

        if self.config.debug == True:
            print('\t-Time Seq Step:')
            print(step)
            self.__printTimeSeq(True)

    def creatPriceMatrix(self):
        """创建代价矩阵
        二维矩阵
            [[-,-,-,-],[],[],...]
                其中，
                    [-,-,-,-]为[任务数量,CPU密集任务数量,IO密集任务数量,集群空闲时间]
                    
                    
        ['10->20->30', 
        '10:12->20:14->30', 
        '10:13->20:14->30', 
        '10:13->20:15->30', 
        
        '10->20->40->50', 
        '10:12->20:14->40:17->50', 
        '10:13->20:14->40:17->50', 
        '10:13->20:15->40:17->50', 
        '10:13->20:15->40:18->50',
        
        '60->50', 
        '60:20->50', 
        '60:21->50', 
        '60:22->50', 
        '60:23->50']   
                    
        """
        visited = self.initVector(100)
        pass

    def __printTimeSeq(self, isReadable):
        """打印时间矩阵
        """
        print('\t-Time Seq Matrix:')
        for r in self.__timeSeq:
            l = []
            for c in r:
                if isReadable:
                    l.append('(' + datetimeUtil.timestamp_datetime(
                        c.get('bdt')) + ',' + datetimeUtil.timestamp_datetime(
                            c.get('edt')) + ')')
                else:
                    l.append(c)

            print(l)

    def printProjects(self):
        print(self.__projects)
