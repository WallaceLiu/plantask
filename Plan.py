# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 09:23:23 2017

@author: liuning11
"""
from TaskAdjMatrix import TaskAdjMatrix
import DateTimeUtil


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
        self._seqMatrix = []
        self._steps = [600, 1200, 1800, 2400, 3000, 3600]
        self._plan = []

    # 开始
    def go(self):
        self.estimate()
        self.__tuning()

    # 评估阶段
    def estimate(self):
        self.__readyEstimate(self._steps)
        self.__count()
        self.__printPlan()

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

    def __count(self):
        def cnt(self, r, c, m, plan):
            for i in range(self._graph.getNodeNum()):
                print('edge=' + str(m[r][i]))
                if m[i][r] == 1:
                    t = self._graph.findRootTask(self._graph.tasksIndex[i])
                    t_bDt = DateTimeUtil.addSec2ts(c.bDateTime, -1 * t.consume)
                    t_eDt = DateTimeUtil.addSec2ts(t_bDt, t.consume)
                    plan[i].append((t_bDt, t_eDt, t.consume))
                    cnt(self, i, t, m, plan)

        print('终端节点：')
        print(self._graph.tTask)

        self.__initPlan()

        for i in range(self._graph.getNodeNum()):
            if self._graph.tTask[i] == 0:
                c = self._graph.findRootTask(self._graph.tasksIndex[i])
                if c.bDateTime != None:
                    self._plan[i].append((c.bDateTime, c.eDateTime, c.consume))
                    cnt(self, i, c, self._graph.map, self._plan)

    # 初始化评估矩阵 
    def __initPlan(self):
        for i in range(self._graph.getNodeNum()):
            self._plan.append([])

    # 统计每时刻任务数据和任务类型数量
    # step 步进时间，单位为分钟
    def __readyEstimate(self, step):
        tasks = self.__sort()
        minmax = self.__getMinMax(tasks)
        print('时间步长：')
        print(self._steps)
        print('任务最早/最晚时间：')
        print(minmax)
        print('时间序列：')
        self.__createSeqMatrix(minmax, self._steps)
        self.__printSeqMatrix()

    # 任务排序
    # 按开始时间排序
    def __sort(self):
        return sorted(self._graph.tasks.tasks, key=lambda x: x.bDateTime)

    # 获得任务中最小和最大时间
    def __getMinMax(self, t):
        l = len(t)
        return (t[0].bDateTime, t[l - 1].bDateTime)

    # 创建时间序列矩阵
    def __createSeqMatrix(self, minmax, step):
        for s in step:
            self._seqMatrix.append(self.__createSeqVector(minmax, s))

    # 创建时间序列向量
    # minmax 最小最大日期
    # step   步长,单位为秒
    def __createSeqVector(self, minmax, step):
        v = []
        b = minmax[0]
        e = None
        while b < minmax[1]:
            e = b + step
            v.append((b, e, 0, 0, 0))
            b = e + 1
        return v

    '''
    打印
    '''

    # 打印时间矩阵
    def __printSeqMatrix(self):
        for r in self._seqMatrix:
            l = []
            for c in r:
                s = '(' + DateTimeUtil.timestamp_datetime(c[
                    0]) + ',' + DateTimeUtil.timestamp_datetime(c[
                        1]) + ',' + str(c[2]) + ',' + str(c[3]) + ',' + str(c[
                            4]) + ')'
                l.append(s)
            print(l)

    # 打印评估时间
    def __printPlan(self):
        print('评估结果：')
        for r in self._plan:
            l = []
            for c in r:
                l.append('(' + DateTimeUtil.timestamp_datetime(c[0]) + ',' +
                         DateTimeUtil.timestamp_datetime(c[1]) + ',' + str(c[
                             2]) + ')')
            print(l)
