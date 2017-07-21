# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:33:41 2017

@author: liuning11
"""


def autoInc(code):
    l = list(code)
    i = len(l) - 1
    while i >= 0:
        if ord(l[i]) + 1 >= 90:
            l[i] = 'A'
            i = i - 1
        else:
            l[i] = chr(ord(l[i]) + 1)
            break
    return ''.join(l)


#if __name__ == '__main__':
#    print(autoincrement('AAAAAA'))
#    print(autoincrement('AAAAAB'))