# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from coreBase import coreBase
import re
from nodeProject import nodeProject


class coreProject(coreBase):

    __regx = ':\d+'
    __no = 0

    def __init__(self):
        pass

    def create(self, oPaths, paths):
        """创建方案结构
        """

        def add(self, pMatrix, p, curTask):
            ts = filter(lambda x: x[1] == p, pMatrix)
            for t in ts:
                if t[1] == p:
                    self.__no = self.__no + 1
                    tp = nodeProject(self.__no, t[0], t[1])
                    curTask.add(tp)

                    if self.config.debug == True and self.config.detail == True:
                        print('\t-Add (%d)(%s) to (%d)(%s)' %
                              (id(tp), tp.toString(), id(curTask),
                               curTask.toString()))

        pMatrix = self.__transform(paths)
        self.__no = 0
        cur = nodeProject()
        root = cur

        for i in range(len(oPaths)):

            add(self, pMatrix, oPaths[i], cur)

            if i < len(oPaths) - 1:
                self.__no = self.__no + 1
                proj = nodeProject(self.__no, str(self.__no), str(self.__no))
                cur.cproject = proj
                cur = proj

        print('\t--Stage: Project...')
        if self.config.debug == True:
            root.printer()
        print('\t--Project End.')
        return root

    def __transform(self, paths):
        p = self.initMatrix2('', len(paths), 2)
        for i in range(len(p)):
            p[i][0] = paths[i]
            p[i][1] = re.sub(self.__regx, '', paths[i], count=0)

        return p
