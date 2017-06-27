# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:40:10 2017

@author: liuning11
"""

from TaskAdjMatrix import TaskAdjMatrix
from Loader import Loader
from LoadParameters import LoadParameters

def DoTest():
    l = Loader('conf/t1.xml')
    g=l.graph
    g.createMap()
    #g.printGraph()
    g.searchPath()
    #g.printPath()   
    #print(g.file)
    #lp=LoadParameters(g)
    g.printGraph()
    t=g.findTask(11)
    print(t.toString(True))


if __name__ == '__main__':
    DoTest()