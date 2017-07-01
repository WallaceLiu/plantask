# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:42:50 2017

@author: liuning11
"""
from LoadConf import LoadConf
from LoadParameters import LoadParameters


class LoadWrapper:
    def __init__(self, path='conf/conf.xml'):
        self.__path = path

    def load(self):
        l = LoadConf(self.__path)
        LoadParameters(l.graph)
        return l.graph
