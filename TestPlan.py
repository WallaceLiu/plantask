# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:37:53 2017

@author: liuning11
"""

from TaskAdjMatrix import TaskAdjMatrix
from Loader import Loader
from LoadParameters import LoadParameters
from Plan import Plan

def DoTest():
    l = Loader('conf/t1.xml')
    g = l.graph
    g.createMap()
    g.searchPath()
    #g.printPath()   
    LoadParameters(g)
    g.printGraph()
    p=Plan(g)
    np =p.sort()
    for t in np:
        print(t.toString(True))
    #g.printRootTasks()

if __name__ == '__main__':
    DoTest()
