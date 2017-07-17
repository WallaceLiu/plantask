# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 10:51:22 2017

general-普通任务
zipper-数据拉链
plumber-数据同步
compute-计算任务
unknown-未知

@author: liuning11
"""
from enum import Enum, unique


@unique
class stageType(Enum):
    LD = 100
    LC = 101
    LP = 102
