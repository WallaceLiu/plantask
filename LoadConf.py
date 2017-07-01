# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:47:40 2017

@author: liuning11
"""
import xml.dom.minidom
from TaskAdjMatrix import TaskAdjMatrix
from Task import Task
from TaskType import TaskType
import time


class LoadConf:

    __path = ""
    __map = []
    graph = TaskAdjMatrix()

    def __init__(self, path="conf/conf.xml"):
        """加载任务配置文件 

        参数:
            path:   任务配置文件，默认值为 conf/conf.xml
        返回:
        异常:
        """
        self.__path = path

        self.__load()

    def __load(self):
        """加载任务配置文件 
        """
        print('Load Conf...')
        try:
            if self.__path == None:
                raise NameError
        except NameError:
            print('Conf File is None')

        DOMTree = xml.dom.minidom.parse(self.__path)
        es = DOMTree.getElementsByTagName("task")
        no = 0
        for e in es:
            no += 1
            t = self.__createTask(e, no)
            self.graph.addTasksIndex(t.id)

            for n in e.childNodes:
                if n.nodeName != "#text":
                    no += 1
                    tc = self.__createTask(n, no)
                    t.childs.add(tc)

                    self.graph.addTasksIndex(tc.id)

            self.graph.addTask(t)

        self.graph.file = self.__path
        self.graph.nodenum = self.__getNodeNum()
        self.graph.edgenum = self.__getEdgeNum()

        self.__printer()
        print('Load Conf Complete.')

    def __createTask(self, e, no):
        """创建任务

        参数:
            e:      xml元素
            no:     序列号，唯一    
        返回:
        异常:
        """
        t = Task(no)
        if e.hasAttribute('id'):
            t.id = e.getAttribute('id')
        if e.hasAttribute('name'):
            t.name = e.getAttribute('name')
        if e.hasAttribute('type'):
            t.type = TaskType.General  #e.getAttribute('type')
        if e.hasAttribute('desc'):
            t.desc = e.getAttribute('desc')
        if e.hasAttribute('executeRule'):
            t.executeRule = e.getAttribute('executeRule')
        if e.hasAttribute('nextExecuteDateTime'):
            v = e.getAttribute('nextExecuteDateTime')
            t.nextExecuteDateTime = time.mktime(
                time.strptime(v, '%Y%m%d%H%M%S')) if len(v) > 0 else None
        if e.hasAttribute('timeout'):
            t.timeout = int(e.getAttribute('timeout'))
        if e.hasAttribute('retryFrequency'):
            t.retryFrequency = int(e.getAttribute('retryFrequency'))
        if e.hasAttribute('retryInterval'):
            t.retryInterval = int(e.getAttribute('retryInterval'))
        if e.hasAttribute('bDateTime'):
            v = e.getAttribute('bDateTime')
            t.bDateTime = time.mktime(time.strptime(
                v, '%Y-%m-%d %H:%M:%S')) if len(v) > 0 else None
        if e.hasAttribute('eDateTime'):
            v = e.getAttribute('eDateTime')
            t.eDateTime = time.mktime(time.strptime(
                v, '%Y-%m-%d %H:%M:%S')) if len(v) > 0 else None
        if e.hasAttribute('consume'):
            t.consume = int(e.getAttribute('consume'))
        if e.hasAttribute('bDateTimeThreshold'):
            t.bDateTimeThreshold = e.getAttribute('bDateTimeThreshold')
        if e.hasAttribute('eDateTimeThreshold'):
            t.eDateTimeThreshold = e.getAttribute('eDateTimeThreshold')

        return t

    def __getNodeNum(self):
        """节点数量
        """
        try:
            if self.graph == None:
                raise AttributeError

            return len(self.graph.tasksIndex)
        except AttributeError:
            print("graph is None.")

    def __getEdgeNum(self):
        """边数量
        """
        try:
            if self.graph == None:
                raise AttributeError

            n = 0
            for t in self.graph.tasks.tasks:
                n += len(t.childs.tasks)
            return n
        except AttributeError:
            print("graph is None.")

    def __printer(self):
        print("Conf File: <%s>, Task Number:<%u>, Edge Number:<%u>" %
              (self.graph.file, self.graph.nodenum, self.graph.edgenum))
        print('Task Id:')
        print(self.graph.tasksIndex)
