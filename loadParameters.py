# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 11:25:05 2017

@author: liuning11
"""

import xml.dom.minidom
import time
from base import base
import datetimeUtil


class loadParameters(base):
    """加载参数
    """

    def __init__(self, g):
        self.__graph = g
        self.path = self.__getParamsFile()
        self.__load()

    def __load(self):
        """
        1，初始化g.lastOccurTime
        """
        try:
            if self.path == None:
                raise NameError
        except NameError:
            print('Conf Params File is None')

        print('--Stage: loadParameters.__load...')
        DOMTree = xml.dom.minidom.parse(self.path)
        es = DOMTree.getElementsByTagName("task")

        for e in es:
            self.__setParamter(e)

        if self.config.debug == True:
            self.__printer()

        print('--loadParameters.__load End.')

    def __setParamter(self, e):
        id = None
        bDt, eDt, c = None, None, None

        if e.hasAttribute('id'):
            id = e.getAttribute('id')
        if e.hasAttribute('bDateTime'):
            bDt = e.getAttribute('bDateTime')
        if e.hasAttribute('eDateTime'):
            eDt = e.getAttribute('eDateTime')
        if e.hasAttribute('consume'):
            c = int(e.getAttribute('consume'))

        try:
            if self.config.debug == True and self.config.detail == True:
                print('\t-loadParameters.__setParamter Find Task <' + id + '>')

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
            print('\t-loadParameters.__setParamter Task <' + id +
                  '> No Found.')

    def __getParamsFile(self):
        if self.__graph == None:
            return None

        p = self.__graph.file.rsplit('.')
        p[0] = p[0] + 'p'
        return '.'.join(p)

    def __printer(self):
        print("\t-Parameter File: <%s>" % self.path)
        print('\t-Root Task: ')
        for t in self.__graph.tasks.tasks:
            print(t.toStringLP())
        print('\t-Last Time When Task Occur:<%s>' %
              (datetimeUtil.timestamp_datetime(self.__graph.lastOccurTime)))
