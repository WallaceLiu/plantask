# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from corePriceBase import corePriceBase


class corePrice(corePriceBase):
    def __init__(self, cm, g):
        corePriceBase.__init__(self, cm, g)

        print('\t-Parameters Ready...')
        self.printParameters()

    def model(self, g):
        """
    
        参数:
        返回:
        异常:
        """
        print('--Stage: corePrice.model...')
        print('--corePrice.model End.')
        pass

    def getProjects(self):
        def isProject(self, s):
            return True

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
                    print('\t-Add Project:%s    %d' % (p, isProj))
                    if isProj:
                        co.append(p)
                    s.pop()

        print('??????????????????????????????????')
        print('--Stage: corePrice.getProjects...')
        self.projOptional.clear()
        s = []
        cur = self.project
        for pro in cur.optional.projects:
            s.append(str(pro.id))
            proj(self, s, cur.cproject, self.projOptional)
            s.pop()

        print(str(len(self.projOptional)))
        print(self.projOptional)
        print('--getProjects End.')

    def price(self, g, path, avgTask):
        """目标函数
        
        计算堆栈中所有节点的目标值
        
        参数:
            s:          权重
            r:    时间间隔向量
            
        返回:
        异常:
        """
        pass
