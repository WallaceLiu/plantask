# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 10:38:47 2017

@author: liuning11
"""
from loadWrapper import loadWrapper
from coreEstimate import coreEstimate
from coreNewAdjMatrix import coreNewAdjMatrix
from corePrice import corePrice


class coreWrapper:
    """任务时间规划
    
    分两个阶段：
    1，评估阶段
    2，调优阶段
    """

    def __init__(self, path='conf/conf.xml'):
        lw = loadWrapper(path)
        g = lw.load()

        g.createMap()
        g.searchPath()

        ce = coreEstimate(g)
        cm = coreNewAdjMatrix(ce)
        p = corePrice(cm, g)
