# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:15:48 2017

@author: liuning11
"""
from TaskType import TaskType
from TaskCollection import TaskCollection
import time


class Task:
    '''
    任务类
    
    no,整型,序号,唯一
    id,整型,标识
    name,字符串,名称
    type,枚举,类型
    desc,字符串,描述
    executeRule,字符串,执行规则,例如：0 10 17 * * ?
    nextExecuteDateTime,下次执行时间,例如：20170621171000
    timeout,整型,超时时间,单位分
    retryFrequency,整型,重试次数
    retryInterval,整型,重试时间间隔,单位秒
    bDateTime,时间类型,开始时间阈值
    eDateTime,时间类型,结束时间阈值
    consume,时间类型,耗时,单位秒
    bDateTimeThreshold,时间类型,开始时间阈值,例如：21:00
    eDateTimeThreshold,时间类型,结束时间阈值,例如：22:00
    childs,子任务集合
    isKey,是否为关键任务
    
    '''

    def __init__(self, no):
        self.no = no
        self.id = ''
        self.name = ''
        self.desc = ''
        self.type = None
        self.executeRule = ''
        self.nextExecuteDateTime = None
        self.timeout = 0
        self.retryFrequency = 0
        self.retryInterval = 0
        self.bDateTime = None
        self.eDateTime = None
        self.consume = 0
        self.bDateTimeThreshold = ''
        self.eDateTimeThreshold = ''
        self.childs = TaskCollection()
        self.isKey = False

    def toString(self, bl):
        s = '<' + str(self.no) + '>'
        s += '\t' + str(self.id)
        s += '\t' + (self.name if len(self.name) > 0 else '-')
        s += '\n\t\t' + '任务类型(' + (str(self.type)
                                   if str(self.type) != None else '-') + ')'
        s += '\n\t\t' + '关键任务(' + str(self.isKey) + ')'
        if bl == True:
            s += '\n\t\t' + '任务描述(' + (self.desc
                                       if len(self.desc) > 0 else '-') + ')'
            s += '\n\t\t' + '运行规则(' + (
                self.executeRule
                if len(self.executeRule) > 0 else '-') + ',' + (
                    time.strftime('%Y-%m-%d %H:%M:%S',
                                  time.localtime(self.nextExecuteDateTime))
                    if self.nextExecuteDateTime != None else '-') + ')'
            s += '\t' + '超时重试(' + str(self.timeout) + ',' + str(
                self.retryFrequency) + ',' + str(self.retryInterval) + ')'
            s += '\n\t\t' + '运行时间(' + (
                time.strftime('%Y-%m-%d %H:%M:%S',
                              time.localtime(self.bDateTime))
                if self.bDateTime != None else '-') + ',' + (
                    time.strftime('%Y-%m-%d %H:%M:%S',
                                  time.localtime(self.eDateTime))
                    if self.eDateTime != None else '-'
                ) + ',' + str(self.consume) + ')'
            s += '\t' + '运行阈值(' + (self.bDateTimeThreshold
                                   if len(self.bDateTimeThreshold) > 0 else '-'
                                   ) + ',' + (self.eDateTimeThreshold
                                              if len(self.eDateTimeThreshold) >
                                              0 else '-') + ')'
        return s

    def printer(self):
        print(self.toString())
        print('\t' + self.childs.printer())

    # 查找任务
    def findTask(self, id):
        if len(self.childs.tasks) > 0:
            return self.childs.findTask(id)

        return None
