# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:15:48 2017

@author: liuning11
"""
from nodeTaskz import nodeTaskz
import time
from base import base


class nodeTask(base):
    """任务类
    
    """

    def __init__(self, no=-1):
        """构造函数

        参数:
            no:                     整型,序号,唯一
            id:                     整型,标识
            name:                   字符串,名称
            type:                   枚举,类型
            desc:                   字符串,描述
            executeRule:            字符串,执行规则,例如：0 10 17 * * ?
            nextExecuteDateTime:    下次执行时间,例如：20170621171000
            timeout:                整型,超时时间,单位分
            retryFrequency:         整型,重试次数
            retryInterval:          整型,重试时间间隔,单位秒
            bDateTime:              时间类型,开始时间阈值
            eDateTime:              时间类型,结束时间阈值
            consume:                时间类型,耗时,单位秒
            bDateTimeThreshold:     时间类型,开始时间阈值,例如：21:00
            eDateTimeThreshold:     时间类型,结束时间阈值,例如：22:00
            childs:                 子任务集合
            isKey:                  是否为关键任务
                
        返回:
        异常:
        """
        self.no = no
        self.id = ''
        self.name = ''
        self.realId = ''
        self.desc = ''
        self.type = None
        self.executeRule = ''
        self.nextExecuteDateTime = None
        self.timeout = 0
        self.retryFrequency = 0
        self.retryInterval = 0
        self.bDateTime = None
        self.eDateTime = None
        self.consume = 1
        self.bDateTimeThreshold = ''
        self.eDateTimeThreshold = ''
        self.childs = nodeTaskz()
        self.isKey = False

    def findTask(self, id):
        """查找任务

        参数:
            id:     整型,标识
                
        返回:
    
        异常:
        """
        if len(self.childs.tasks) > 0:
            return self.childs.findTask(id)

        return None

    def clone(self):
        t = nodeTask()
        t.no = self.no
        t.id = self.id
        t.realId = self.realId
        t.name = self.name
        t.desc = self.desc
        t.type = self.type
        t.executeRule = self.executeRule
        t.nextExecuteDateTime = self.nextExecuteDateTime
        t.timeout = self.timeout
        t.retryFrequency = self.retryFrequency
        t.retryInterval = self.retryInterval
        t.bDateTime = self.bDateTime
        t.eDateTime = self.eDateTime
        t.consume = self.consume
        t.bDateTimeThreshold = self.bDateTimeThreshold
        t.eDateTimeThreshold = self.eDateTimeThreshold
        t.childs = self.childs.clone()
        t.isKey = self.isKey
        return t

    def cloneLocal(self):
        t = nodeTask()
        t.no = self.no
        t.id = self.id
        t.realId = self.realId
        t.name = self.name
        t.desc = self.desc
        t.type = self.type
        t.executeRule = self.executeRule
        t.nextExecuteDateTime = self.nextExecuteDateTime
        t.timeout = self.timeout
        t.retryFrequency = self.retryFrequency
        t.retryInterval = self.retryInterval
        t.bDateTime = self.bDateTime
        t.eDateTime = self.eDateTime
        t.consume = self.consume
        t.bDateTimeThreshold = self.bDateTimeThreshold
        t.eDateTimeThreshold = self.eDateTimeThreshold
        t.childs = nodeTaskz()
        t.isKey = self.isKey
        return t

    """
    打印
    """

    def toStringBrief(self):
        """输出no，id，realid，name
        """
        s = '<' + str(self.no) + '>'
        s += '\t' + str(self.id)
        s += '\t' + str(self.realId)
        s += '\t' + (self.name if len(self.name) > 0 else '-')

        return s

    def toStringDesc(self):
        """输出no，id，realid，name，desc
        """
        s = '<' + str(self.no) + '>'
        s += '\t' + str(self.id)
        s += '\t' + str(self.realId)
        s += '\t' + (self.name if len(self.name) > 0 else '-')
        s += '\t' + self.desc

        return s

    def toStringTy(self):
        """输出type，iskey
        """
        s = '\t' + '任务类型(' + (str(self.type)
                              if str(self.type) != None else '-') + ')'
        s += '\t' + '关键任务(' + str(self.isKey) + ')'
        return s

    def toStringRR(self):
        """输出运行规则Run Rule
        """
        s = '\t' + '运行规则(' + (
            self.executeRule if len(self.executeRule) > 0 else '-') + ',' + (
                time.strftime('%Y-%m-%d %H:%M:%S',
                              time.localtime(self.nextExecuteDateTime))
                if self.nextExecuteDateTime != None else '-') + ')'
        s += '\t' + '超时重试(' + str(self.timeout) + ',' + str(
            self.retryFrequency) + ',' + str(self.retryInterval) + ')'
        s += '\t' + '运行阈值(' + (self.bDateTimeThreshold
                               if len(self.bDateTimeThreshold) > 0 else '-'
                               ) + ',' + (self.eDateTimeThreshold
                                          if len(self.eDateTimeThreshold) > 0
                                          else '-') + ')'
        return s

    def toStringRT(self):
        """输出运行时间Run Time
        """
        s = '\t' + '运行时间(' + (
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.bDateTime))
            if self.bDateTime != None else '-'
        ) + ',' + (
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(self.eDateTime))
            if self.eDateTime != None else '-') + ',' + str(self.consume) + ')'
        return s

    def toStringLC(self):
        """输出LoadConf阶段加载的信息
        """
        s = self.toStringBrief()
        s += self.toStringTy()
        s += self.toStringRR()

        return s

    def toStringLP(self):
        """输出LoadParameter阶段加载的信息
        """
        s = self.toStringBrief()
        s += self.toStringRT()

        return s

    def toString(self):
        s = self.toStringDesc()
        s += self.toStringTy()
        s += self.toStringRR()
        s += self.toStringRT()

        return s
