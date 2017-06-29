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
    LoadParameters(l.graph)
    g.printGraph()


if __name__ == '__main__':
    DoTest()
