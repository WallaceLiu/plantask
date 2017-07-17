# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:43:31 2017

@author: liuning11
"""
from coreNewAdj import coreNewAdj
from nodeAdjMatrix import nodeAdjMatrix
import datetimeUtil
import random


class coreNewAdjMatrix(coreNewAdj):
    """创建新的任务图
    
    根据对每个任务的最晚开始时间
    
    """

    minmax = None
    modelGraph = nodeAdjMatrix()

    def __init__(self, g):
        coreNewAdj.__init__(self, g)

        print('--Stage: coreNewAdjMatrix...')

        self.minmax = self.__getMinMax(self.graph.lastOccurTime)

        self.__create(g, self.minmax)

        self.__search(self.modelGraph)

        self.__cut(self.modelGraph)

        print('--Stage: coreNewAdjMatrix End.')

    def __create(self, g, minmax):
        """添加新的可能的任务节点，并创建邻接矩阵
        """

        def ready(self, g, step, minmax):

            if self.config.debug == True:
                print('\t-coreNewAdjMatrix.__create.ready...')
                print('\t\t-Min and Max:<%s,%s>' %
                      (datetimeUtil.timestamp_datetime(minmax[0]),
                       datetimeUtil.timestamp_datetime(minmax[1])))

            no = g.edgenum + g.nodenum + 1
            arr = []
            for i in range(g.nodenum):
                if g.tTask[i] == 1:  # 非终端任务节点
                    t = g.findRootTask(g.tasksIndex[i])
                    bDt = t.bDateTime - step
                    win = maxParentConsume(self, g.map, g.nodenum, i)

                    if self.config.debug == True and self.config.detail == True:
                        print(
                            '\t\t-ready:%s      win=%s      end=%s    step=%s'
                            %
                            (t.id, win,
                             datetimeUtil.timestamp_datetime(minmax[0] + win),
                             str(step)))

                    while bDt > minmax[0] + win:
                        nt = t.cloneLocal()
                        nt.no = no
                        nt.id = nt.id + ':' + str(no)  # 新ID=原ID+序号
                        nt.bDateTime = bDt
                        nt.eDateTime = nt.bDateTime + nt.consume

                        arr.append(nt)

                        if self.config.debug == True:
                            print('\t\t\t-Add New:%s' % nt.toStringRT())

                        bDt = bDt - step
                        no = no + 1

            if self.config.debug == True:
                print('\t-coreNewAdjMatrix.__create.ready:')
                for a in arr:
                    print(a.toStringLP())

            return arr

        def maxParentConsume(self, matrix, nodenum, c):
            m = 0
            r = c
            consume = 0
            while r >= 0:
                rt = -1
                for i in range(nodenum):
                    if matrix[i][r] > m:
                        m = matrix[i][r]
                        rt = i
                if rt > 0:
                    consume += m
                r = rt

            return consume

        def create(self, g, step, minmax):
            """添加新的肯能的任务节点，并创建新的邻接矩阵任务图
            """
            t_arrs = ready(self, g, step, minmax)

            ng = g.clone()

            no = t_arrs[len(t_arrs) - 1].no + 1

            for t_arr in t_arrs:  # 添加节点
                n = t_arr.cloneLocal()
                ng.add(ng.tasks, n)
                no = no + 1

                node = ng.findRootTask(t_arr.realId)

                for c in node.childs.tasks:  # 添加节点边
                    t = ng.findRootTask(c.realId)

                    if len(t.childs.tasks) == 0:
                        ng.add(n.childs, t.cloneLocal())  # 添加终端节点的边
                    else:
                        edges = filter(
                            lambda x: t.realId == x.realId and t_arr.eDateTime <= x.bDateTime,
                            t_arrs)

                        for edge in edges:
                            e = edge.cloneLocal()
                            ng.add(n.childs, e)

            ng.createMap()
            return ng

        print('\t-coreNewAdjMatrix.__create...')
        self.modelGraph = create(self, g, self.config.timeStep, minmax)
        print('\t-coreNewAdjMatrix.__create End.')

    def __moving(self, step):
        """随机时间
            避免在移动任务时，都聚集在一个时间点
            
        参数:
            step:   时间间隔
        """
        seed = random.randint(0, 100)
        return int(step * (1 + seed / 100))

    def __getMinMax(self, lastOccurTime):
        """获得任务中最早最晚时间
        """
        minmax = (lastOccurTime - self.config.period * 3600, lastOccurTime)

        return minmax

    def __search(self, g):
        """查找邻接矩阵所有路径
        """

        def m(self, s, r):
            for i in range(g.nodenum):
                if g.map[r][i] > 0:
                    s.append(g.tasksIndex[i])
                    m(self, s, i)
                    s.pop()
                else:
                    if i >= g.nodenum - 1:
                        if self.__isPath(g, s) is True:
                            p = '->'.join(s)
                            self.path.append(p)

        print('--Stage: coreNewAdjMatrix.__search...')
        s = []
        for r in range(g.nodenum):
            s.clear()
            if g.rTask[r] == 0:
                s.append(g.tasksIndex[r])
                m(self, s, r)

        if self.config.debug == True:
            print(self.path)

        print('--coreNewAdjMatrix.__search End.')

    def __isPath(self, g, s):
        """是否为一个任务路径
        """

        def _isExist(self, g, s):
            """是否已经存在
            """
            path = '->'.join(s)
            for p in self.path:
                if path in p:
                    return True
            return False

        def _isRoot(self, g, botomm):
            """是否为根节点
            只有是根节点开头的才是路径
            """
            bl = g.isRootTask(botomm.split(':')[0])
            if bl is False:
                pass  # 删除边

            return bl

        return _isExist(self, g, s) is False and _isRoot(self, g, s[0]) is True

    def __cut(self, g):
        """新创建任务图中与路径是有矛盾的，需要删除不用的边，重新创建完整正确的任务图
        """
        pass

    """
    打印
    """
