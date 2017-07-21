# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:03:00 2017

@author: liuning11
"""


def lcsse_len(s1, s2):
    """最长公共子序列长度
    """
    m = [[0 for x in s2] for y in s1]
    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                if p1 == 0 or p2 == 0:
                    m[p1][p2] = 1
                else:
                    m[p1][p2] = m[p1 - 1][p2 - 1] + 1
            elif m[p1 - 1][p2] < m[p1][p2 - 1]:
                m[p1][p2] = m[p1][p2 - 1]
            else:  # m[p1][p2-1] < m[p1-1][p2]
                m[p1][p2] = m[p1 - 1][p2]
    return m[-1][-1]


def lcsse(s1, s2):
    """最长公共子序列
    """
    # length table: every element is set to zero.
    m = [[0 for x in s2] for y in s1]
    # direction table: 1st bit for p1, 2nd bit for p2.
    d = [[None for x in s2] for y in s1]
    # we don't have to care about the boundery check.
    # a negative index always gives an intact zero.
    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                if p1 == 0 or p2 == 0:
                    m[p1][p2] = 1
                else:
                    m[p1][p2] = m[p1 - 1][p2 - 1] + 1
                d[p1][p2] = 3  # 11: decr. p1 and p2
            elif m[p1 - 1][p2] < m[p1][p2 - 1]:
                m[p1][p2] = m[p1][p2 - 1]
                d[p1][p2] = 2  # 10: decr. p2 only
            else:  # m[p1][p2-1] < m[p1-1][p2]
                m[p1][p2] = m[p1 - 1][p2]
                d[p1][p2] = 1  # 01: decr. p1 only
    (p1, p2) = (len(s1) - 1, len(s2) - 1)
    # now we traverse the table in reverse order.
    s = []
    while 1:
        #print p1, p2
        c = d[p1][p2]
        if c == 3: s.append(s1[p1])
        if not ((p1 or p2) and m[p1][p2]): break
        if c & 2: p2 -= 1
        if c & 1: p1 -= 1
    s.reverse()
    return ''.join(s)


def lcsst(s1, s2):
    """最长公共子字符串
    """
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    mmax = 0  #最长匹配的长度  
    p = 0  #最长匹配对应在s1中的最后一位  
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1
    return s1[p - mmax:p], mmax


def rlcsst(s1, s2):
    """限制的最长公共子字符串
    """
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    mmax = 0  #最长匹配的长度  
    p = 0  #最长匹配对应在s1中的最后一位  
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > mmax:
                    mmax = m[i + 1][j + 1]
                    p = i + 1

    if p - mmax != 0:
        return '', -1

    return s1[p - mmax:p], mmax


if __name__ == '__main__':
    #print(find_lcs('10->20->30', '10:12->20:14->40:17->50'))
    #print(find_lcs_len('abcoisjf', 'axbaoeijf'))
    print(rlcsst('10->20->30', '10:12->20:14->40:17->50'))
    print(rlcsst('10:13->20:14->30', '10:13->20:15->40:17->50'))
