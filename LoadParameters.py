# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 11:25:05 2017

@author: liuning11
"""

import xml.dom.minidom
from TaskAdjMatrix import TaskAdjMatrix
from Task import Task
import time
from base import base


class LoadParameters(base):
    """加载参数
    
    包括,开始时间bDateTime,结束时间eDateTime,耗时consume
    """

    def __init__(self, g):
        self.__graph = g
        self.__path = self.__createFile()
        self.__load()

    def __load(self):
        try:
            if self.__path == None:
                raise NameError
        except NameError:
            print('Conf File is None')

        print('--Stage Load Paramter...')
        DOMTree = xml.dom.minidom.parse(self.__path)
        es = DOMTree.getElementsByTagName("task")

        for e in es:
            self.__setParamter(e)

        if self.config.debug == True:
            self.__printer()

        print('--Load Paramter Complete.')

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
            if self.config.debug == True:
                print('\t-Find...Task <' + id + '>')

            t = self.__graph.findRootTask(id)
            if t == None:
                raise NameError
            else:
                t.bDateTime = time.mktime(
                    time.strptime(bDt, '%Y-%m-%d %H:%M:%S')) if len(
                        bDt) > 0 else None
                t.eDateTime = time.mktime(
                    time.strptime(eDt, '%Y-%m-%d %H:%M:%S')) if len(
                        eDt) > 0 else None
                t.consume = c

                self.__graph.setLastOccurTime(t)

        except NameError:
            print('-Task <' + id + '> No Found, is None')

    def __createFile(self):
        if self.__graph == None:
            return None

        p = self.__graph.file.rsplit('.')
        p[0] = p[0] + 'p'
        return '.'.join(p)

    def __printer(self):
        print('\t-Root Task: ')
        for t in self.__graph.tasks.tasks:
            print(t.toStringParams())
        self.__graph.printLastOccurTime()
