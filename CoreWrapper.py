# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 10:38:47 2017

@author: liuning11
"""
from LoadWrapper import LoadWrapper
from CoreEstimate import CoreEstimate
from CoreModelByTaskNum import CoreModelByTaskNum


class CoreWrapper:
    """任务时间规划
    
    分两个阶段：
    1，评估阶段
    2，调优阶段
    """

    def __init__(self, path='conf/conf.xml'):
        l = LoadWrapper(path)
        g = l.load()
        g.createMap()
        g.searchPath()
        e = CoreEstimate(g)
        #m = CoreModelByTaskNum(e)
        #m.models()
