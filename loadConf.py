# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:47:40 2017

@author: liuning11
"""
import xml.dom.minidom
from nodeAdjMatrix import nodeAdjMatrix
from nodeTask import nodeTask
from nodeTaskType import nodeTaskType
import time
from base import base


class loadConf(base):

    __path = ""
    graph = nodeAdjMatrix()

    def __init__(self, path):
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
            1，初始化g.tasksIndex
            2，初始化g.tasks
        """
        print('--Stage: loadConf.__load...')
        try:
            if self.__path == None:
                raise NameError
        except NameError:
            print('\t-Conf File is None')

        DOMTree = xml.dom.minidom.parse(self.__path)
        es = DOMTree.getElementsByTagName("task")
        no = 0

        for e in es:
            no += 1
            t = self.__createTask(e, no)

            self.graph.add(self.graph.tasks, t)

            for n in e.childNodes:
                if n.nodeName != "#text":
                    no += 1
                    tc = self.__createTask(n, no)
                    self.graph.add(t.childs, tc)

        self.graph.file = self.__path

        if self.config.debug == True:
            self.__printer()

        print('--loadConf.__load End.')

    def __createTask(self, e, no):
        """创建任务

        参数:
            e:      xml元素
            no:     序列号，唯一    
        返回:
        异常:
        """
        t = nodeTask(no)
        if e.hasAttribute('id'):
            t.id = e.getAttribute('id')
            t.realId = t.id
        if e.hasAttribute('name'):
            t.name = e.getAttribute('name')
        if e.hasAttribute('type'):
            t.type = nodeTaskType.General  #e.getAttribute('type')
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

    def __printer(self):
        self.graph.printTasksIndex()
