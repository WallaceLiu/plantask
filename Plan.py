# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:23:23 2017

@author: liuning11
"""
from TaskAdjMatrix import TaskAdjMatrix


class Plan:
    '''
    时间规划
    
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
    '''

    def __init__(self, g):
        self._graph = g

    # 开始
    def go(self):
        self.__estimate()
        self.__tuning()

    # 评估阶段
    def __estimate(self):
        pass

    # 调优阶段
    def __tuning(self):
        pass

    # 根据每个时间段的任务数量调优
    def __tunningByTaskNum(self):
        pass

    # 根据每个时间段的任务类型调优
    def __tunningByTaskType(self):
        pass

    # 取最早的时间
    def __min(self):
        pass

    # 排序
    # 按开始时间排序
    def sort(self):
        return sorted(self._graph.tasks.tasks, key=lambda x: x.bDateTime)

    # 获得任务中最小和最大时间
    def getMinMax(self, t):
        l = len(t)
        return (t[0].bDateTime, t[l - 1].bDateTime)

    # 统计每时刻任务数据和任务类型数量
    # step 步进时间，单位为分钟
    def __stat(self, step):
        ts = self._graph.tasks
