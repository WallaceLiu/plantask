# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from base import base
import datetimeUtil


class corePriceBase(base):

    __minmax = None
    __steps = None
    __period = None
    __stepNum = []
    __path = []
    __modelGraph = []
    __timeSeq = []
    __priceMatrix = []

    def __init__(self, cm):
        self.__minmax = cm.estimate.minmax
        self.__steps = cm.estimate.steps
        self.__period = cm.estimate.period
        self.__path = cm.path
        self.__modelGraph = cm.estimate.modelGraph

        self.initStepNum(self.__steps, self.__period)
        self.initTimeSeq(self.__steps, self.__minmax)

        self.__priceMatrix = self.initMatrix2(len(self.__timeSeq[0]), 4)

    def price():
        """代价计算
        """
        pass

    def printParameters(self):
        print('\t\t-coreNewAdjMatrix.estimate.minmax:')
        print('(%s, %s)' % (
            (datetimeUtil.timestamp_datetime(self.__minmax[0]),
             datetimeUtil.timestamp_datetime(self.__minmax[1]))))
        print('\t\t-coreNewAdjMatrix.estimate.steps:')
        print(self.__steps)
        print('\t\t-coreNewAdjMatrix.estimate.period:')
        print(self.__period)
        print('\t\t-corePrice.stepNum:')
        print(self.__stepNum)
        print('\t\t-coreNewAdjMatrix.path:')
        print(self.__path)
        print('\t\t-coreNewAdjMatrix.estimate.modelGraph:')
        print(self.__modelGraph[0].printGraph())
        self.__printTimeSeq(True)
        #for m in self.__priceMatrix:
        print(self.__priceMatrix)

    def initStepNum(self, steps, period):
        """初始化时间间隔数量
                
            按开始时间排序
        
        参数:
            step:   步进时间，单位为秒
            g:      任务图
        返回:
    
        异常:
                
        """
        for step in steps:
            self.__stepNum.append(int(period * 3600 / step) + 1)

        if self.config.debug == True:
            print('\t-corePrice.__initStepNum:')
            print(self.__stepNum)

    def initTimeSeq(self, steps, minmax):
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

        for s in self.__steps:
            self.__timeSeq.append(createTimeSeqVector(self, minmax, s))

        if self.config.debug == True:
            print('\t-Time Seq Step:')
            print(steps)
            self.__printTimeSeq(True)

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
