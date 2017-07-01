# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:19:45 2017

@author: liuning11
"""

from TaskAdjMatrix import TaskAdjMatrix
from LoadWrapper import LoadWrapper


def DoTest():
    l = LoadWrapper("conf/t1.xml")
    g = l.load()
    g.createMap()
    g.printMap()
    g.searchPath()
    g.printPath()
    #p = g.findPathByStr('5')
    #print(p)
    #p = g.findPathByStr('1')
    #print(p)

#    print("广度优先遍历")
#    g.BreadthFirstSearch()
#    print("深度优先遍历")
#    g.DepthFirstSearch()


if __name__ == '__main__':
    DoTest()
