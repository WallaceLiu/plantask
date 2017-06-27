# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 11:25:05 2017

@author: liuning11
"""

import xml.dom.minidom
from TaskAdjMatrix import TaskAdjMatrix
from Task import Task
import time


class LoadParameters:
    '''
    加载参数，
    包括开始时间bDateTime，结束时间eDateTime，耗时consume
    '''

    def __init__(self, g):
        self.__graph = g
        self.__path = self.__createFile()
        self.__load()

    def __load(self):
        DOMTree = xml.dom.minidom.parse(self.__path)
        es = DOMTree.getElementsByTagName("task")

        print(self.__graph.tasksIndex)
        for e in es:
            self.__setParamter(e)

        # 创建任务
    def __setParamter(self, e):
        id = None
        bDt = None
        eDt = None
        c = None

        if e.hasAttribute('id'):
            id = e.getAttribute('id')
        if e.hasAttribute('bDateTime'):
            bDt = e.getAttribute('bDateTime')
        if e.hasAttribute('eDateTime'):
            eDt = e.getAttribute('eDateTime')
        if e.hasAttribute('consume'):
            c = int(e.getAttribute('consume'))

        try:
            print('Find...Task <' + id + '>')
            t = self.__graph.findRootTask(id)
            if t == None:
                raise IndexError
            else:
                t.bDateTime = time.mktime(
                    time.strptime(bDt, '%Y-%m-%d %H:%M:%S')) if len(
                        bDt) > 0 else None
                t.eDateTime = time.mktime(
                    time.strptime(eDt, '%Y-%m-%d %H:%M:%S')) if len(
                        eDt) > 0 else None
                t.consume = c

        except IndexError:
            print('Task <' + id + '> No Found, is None')

    def __createFile(self):
        p = self.__graph.file.rsplit('.')
        p[0] = p[0] + 'p'
        return '.'.join(p)
