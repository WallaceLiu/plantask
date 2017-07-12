# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:42:50 2017

@author: liuning11
"""
from loadConf import loadConf
from loadParameters import loadParameters


class loadWrapper:
    def __init__(self, path='conf/conf.xml'):
        self.__path = path

    def load(self):
        l = loadConf(self.__path)
        loadParameters(l.graph)
        return l.graph
