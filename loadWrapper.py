# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:42:50 2017

@author: liuning11
"""
from loadConf import loadConf
from loadParameters import loadParameters


class loadWrapper:

    configPath = None
    configParamsPath = None

    def __init__(self, path):
        self.configPath = path

    def load(self):
        lc = loadConf(self.configPath)
        lp = loadParameters(lc.graph)

        self.configParamsPath = lp.path
        return lc.graph
