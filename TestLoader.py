# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:50:29 2017

@author: liuning11
"""
from Loader import Loader


def DoTest():
    l = Loader("conf/t1.xml")
    g = l.graph
    g.printGraph()


if __name__ == '__main__':
    DoTest()
