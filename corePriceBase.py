# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from coreBase import coreBase
import datetimeUtil
from nodeProject import nodeProject
from coreProject import coreProject


class corePriceBase(coreBase):

    __regx = ':\d+'
    __no = 0
    __minmax = None
    stepNum = None
    __originalPath = []
    __path = []
    modelGraph = None
    __timeSeq = []
    priceMatrix = []
    project = nodeProject()
    projOptional = []

    def __init__(self, cm, g):
        self.__minmax = cm.minmax
        self.__originalPath = g.path
        self.__path = cm.path
        self.modelGraph = cm.modelGraph

        print('--Stage: corePrice...')

        self.__initStepNum(self.config.timeStep, self.config.period)
        self.__initTimeSeq(self.config.timeStep, self.__minmax)

        self.priceMatrix = self.__initpriceMatrix(
            0, self.stepNum, self.config.priceDim, self.__timeSeq)

        self.__createProject(self.__originalPath, self.__path)

    def __createProject(self, opaths, paths):
        """创建方案结构
        """
        cp = coreProject()
        self.project = cp.create(self.__originalPath, self.__path)

    def __initStepNum(self, step, period):
        """初始化时间间隔数量
        """
        self.stepNum = None
        self.stepNum = int(period * 3600 / step) + 1

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
                v.append((b, e))
                b = e + 1
            return v

        self.__timeSeq.clear()
        self.__timeSeq = createTimeSeqVector(self, minmax, step)

    def __initpriceMatrix(self, v, rn, cn, tv):
        m = self.initMatrix2(0, self.stepNum, self.config.priceDim)

        for i in range(len(tv)):
            m[i].append(tv[i])

        return m

    def printParameters(self):
        print('\t\t-Min And Max:')
        print('(%s, %s)' % (
            (datetimeUtil.timestamp_datetime(self.__minmax[0]),
             datetimeUtil.timestamp_datetime(self.__minmax[1]))))
        print('\t\t-Time Step: %d' % (self.config.timeStep))
        print('\t\t-Period: %d' % (self.config.period))
        print('\t\t-Step Num: %d' % (self.stepNum))
        print('\t\t-Original Path:')
        print(self.__originalPath)
        print('\t\t-Path:')
        print(self.__path)
        self.__printTimeSeq(True)
        print('\t\t-Price Matrix:')
        print(self.priceMatrix)
        #print('\t\t-coreNewAdjMatrix.estimate.modelGraph:')
        #print(self.modelGraph.printGraph())
        print('\t\t-projects:')
        self.project.printer()

    def __printTimeSeq(self, isReadable):
        """打印时间矩阵
        """
        print('\t-Time Seq Vector:')
        for r in self.__timeSeq:
            if isReadable:
                print('(' + datetimeUtil.timestamp_datetime(r[0]) + ',' +
                      datetimeUtil.timestamp_datetime(r[1]) + ')')
            else:
                print(r)
