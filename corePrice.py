# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from corePriceBase import corePriceBase
import lcs


class corePrice(corePriceBase):
    def __init__(self, cm, g):
        corePriceBase.__init__(self, cm, g)

        print('\t-Parameters Ready...')
        self.printParameters()

    def model(self, g):
        """
        """
        print('--Stage: corePrice.model...')
        print('--corePrice.model End.')
        pass

    def getProjects(self):
        def isProject(self, s):
            j = 0
            for i in range(len(s) - 1):
                # 具有最大公共子串，并且第一个任务相同
                if lcs.rlcsst(
                        s[i], s[i + 1]) <= 0 and s[i].split('->')[0].split(
                            ':')[0] == s[i + 1].split('->')[0].split(':')[0]:
                    break
                j = i

            if j >= len(s) - 2:
                return True

            return False

        def proj(self, s, c, co):
            for pro in c.optional.projects:
                s.append(str(pro.id))
                if c.cproject != None:
                    cur = c.cproject
                    proj(self, s, cur, co)
                    s.pop()
                else:
                    p = '$'.join(s)
                    isProj = isProject(self, s)

                    if self.config.debug == True and self.config.detail == True:
                        print('\t-Add Project:%s    %d' % (p, isProj))

                    if isProj:
                        co.append(p)

                    s.pop()

        print('--Stage: corePrice.getProjects...')
        self.projOptional.clear()
        s = []
        cur = self.project
        for pro in cur.optional.projects:
            s.append(str(pro.id))
            proj(self, s, cur.cproject, self.projOptional)
            s.pop()

        if self.config.debug == True:
            print('\t-Project Number: %d' % (len(self.projOptional)))
            print(self.projOptional)
        print('--getProjects End.')

        self.stat(self.modelGraph, self.projOptional[0], self.priceMatrix)
        print(self.priceMatrix)

    def stat(self, g, project, priceMatrix):
        st = set(project.replace('->', '\t').replace('$', '\t').split('\t'))
        for s in st:
            t = g.findRootTask(s)
            i = 0
            while i < len(priceMatrix):
                if t.bDateTime < priceMatrix[i][4][0]:
                    break

                i = i + 1

            while i < len(priceMatrix) and t.eDateTime != None:
                if t.eDateTime <= priceMatrix[i][4][1]:
                    priceMatrix[i][0] = priceMatrix[i][0] + 1
                    #按任务类型统计任务数量
                    #priceMatrix[i][1] = priceMatrix[i][1] + 1
                    #priceMatrix[i][2] = priceMatrix[i][2] + 1
                else:
                    break

                i = i + 1

    def price(self, priceMatrix, stepNum):
        """目标函数
        
        计算堆栈中所有节点的目标值
        
        参数:
            s:          权重
            r:    时间间隔向量
            
        返回:
        异常:
        """

        pass
