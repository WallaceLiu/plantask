# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 11:37:53 2017

@author: liuning11
"""

from Loader import Loader
from LoadParameters import LoadParameters
from Plan import Plan


def DoTest():
    l = Loader('conf/t1.xml')
    g = l.graph
    g.createMap()
    LoadParameters(g)
    g.printGraph()
    p = Plan(g)
    p.estimate()
    


if __name__ == '__main__':
    DoTest()
