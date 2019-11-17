# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 09:47:35 2017

@author: liuning11
"""
from base import base


class nodeProjectz(base):
    '''
    任务集合类
    '''

    def __init__(self):
        self.projects = []

    def add(self, pro):
        self.projects.append(pro)

    def clear(self):
        self.projects.clear()

    def printer(self, tab):
        for p in self.projects:
            print(tab + p.toString())
