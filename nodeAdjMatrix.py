# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:15:48 2017

@author: liuning11
"""

from nodeTaskz import nodeTaskz
from nodeAdjBase import nodeAdjBase
from stageType import stageType


class nodeAdjMatrix(nodeAdjBase):
    """邻接矩阵
    
    a->b->c
    a->b->d->e
    f->e
    
      a b c d e f
    a 0 1 0 0 0 0
    b 0 0 1 1 0 0
    c 0 0 0 0 0 0
    d 0 0 0 0 1 0
    e 0 0 0 0 0 0
    f 0 0 0 0 1 0

    若列全为0，则表示为根节点
    若行全为0，则表示为终端节点，无子节点
    
    """

    def __init__(self):
        """构造函数

        参数:
            tasksIndex:     所有节点ID
            tasks:          所有节点实例
            rTask:          根节点
                            列全为0
            tTask:          终端节点
                            行全为0
            nodenum:        节点数量
            edgenum:        边数量
            map:            邻接矩阵
            path:           节点配置文件
            file:           节点配置文件
            lastOccurTime:  最晚任务时间
        返回:
        异常:
        """
        self.tasksIndex = []
        self.tasks = nodeTaskz()
        self.rTask = []
        self.tTask = []
        self.nodenum = 0
        self.edgenum = 0
        self.map = []
        self.path = []
        self.file = None
        self.lastOccurTime = 0.0

    def createMap(self):
        """创建邻接矩阵
            1，初始化nodenum
            2，初始化edgenum
            3，初始化map
            4，初始化tTask
            5，初始化rTask
        """

        def before(self):
            """初始化邻接矩阵
            """

            self.nodenum = self.getNodeNum()
            self.edgenum = self.getEdgeNum()

            self.map = nodeAdjBase.initMatrix2(self, 0, self.nodenum,
                                               self.nodenum)

        def create(self):
            """创建邻接矩阵
            """
            self.rTask = [0] * self.nodenum
            self.tTask = [0] * self.nodenum

            for x in self.tasks.tasks:
                w = self.__findIndex(x.id)
                for y in x.childs.tasks:
                    v = self.__findIndex(y.id)
                    self.addEdge(w, v, x.consume)

                    self.tTask[w] = 1
                    self.rTask[v] = 1

        def after(self):
            """在邻接矩阵行-列追加所有任务ID
            """
            for i in range(self.nodenum):
                self.map[i].append(self.tasksIndex[i])

            self.map.append(self.tasksIndex)

        self.map = []
        before(self)
        create(self)
        #after(self)

        print('--Stage: nodeAdjMatrix.createMap...')
        if self.config.debug == True:
            self.printGraph()
        print('--nodeAdjMatrix.createMap End.')

    def searchPath(self):
        """查找邻接矩阵所有路径
        1，初始化path
        """

        def isPath(self, path):
            """是否为一个任务路径
            """
            for p in self.path:
                if path in p:
                    return True
            return False

        def path(self, s, r):
            for i in range(self.nodenum):
                if self.map[r][i] > 0:
                    s.append(self.tasksIndex[i])
                    path(self, s, i)
                    s.pop()
                else:
                    if i >= self.nodenum - 1:
                        p = '->'.join(s)
                        if isPath(self, p) == False:
                            self.path.append(p)

        s = []
        for r in range(len(self.rTask)):
            s.clear()
            if self.rTask[r] == 0:
                s.append(self.tasksIndex[r])
                path(self, s, r)

        print('--Stage: nodeAdjMatrix.searchPath...')
        if self.config.debug == True:
            self.printPath()
        print('--nodeAdjMatrix.searchPath End.')

    def isRootTask(self, id):
        """是否为根节点
        """
        for i in range(self.nodenum):
            if self.rTask[i] == 0 and self.tasksIndex[i] == id:
                return True
        return False

    def add(self, p, t):
        """添加任务

        参数:
            t:  添加任务
        返回:
        异常:
        """

        def addIndex(self, taskId):
            """添加任务ID 
            """

            def isExist(self, taskId):
                """判断任务Id是否已经存在
                """
                for id in self.tasksIndex:
                    if id == taskId:
                        return True
                return False

            if len(self.tasksIndex) <= 0:
                self.tasksIndex.append(taskId)
            else:
                if isExist(self, taskId) == False:
                    self.tasksIndex.append(taskId)

        #self.tasks.add(t)

        p.add(t)
        addIndex(self, t.id)

    def setLastOccurTime(self, t):
        if t.bDateTime != None:
            self.lastOccurTime = t.bDateTime if t.bDateTime > self.lastOccurTime else self.lastOccurTime

    def __findIndex(self, id):
        """查找指定节点的行列索引
        
        参数:
            id:     任务Id
        """
        for i in range(len(self.tasksIndex)):
            if id == self.tasksIndex[i]:
                return i

    def __isOutRange(self, x):
        try:
            if x >= self.nodenum or x <= 0:
                raise IndexError
        except IndexError:
            print("节点下标出界")

    def addEdge(self, x, y, weight):
        """添加边

        参数:
            x:  row
            y:  column
        返回:
        异常:
        """
        self.map[x][y] = weight

    def removeEdge(self, x, y):
        """删除边

        参数:
            x:  row
            y:  column
        返回:
        异常:
        """
        if self.map[x][y] is 0:
            self.map[x][y] = 0
            self.edgenum = self.edgenum - 1

    def findChildByMatrix(self, id):
        """查找指定节点的所有直接子节点

        参数:
            id:     任务Id
        返回:
        异常:
        """
        n = []
        r = self.__findIndex(id)
        for i in range(self.getNodeNum()):
            if self.map[r][i] == 1:
                n.append(self.map[r][i])

        return n

    def findParentByMatrix(self, id):
        """查找指定节点的直接父节点

        参数:
            id:     任务Id
        返回:
        异常:
        """
        n = []
        r = self.__findIndex(id)
        for i in range(self.getNodeNum()):
            if self.map[i][r] == 1:
                n.append(self.map[i][r])

        return n

    def findPathByStr(self, id):
        """根据路径集合检索
        
        参数:
            id:     任务Id
        """
        l = []
        for p in self.path:
            if '->' + id in p or id + '->' in p:
                l.append(p)
        return l

    def sortBDateTime(self, tasks):
        return sorted(tasks, key=lambda x: x.bDateTime)

    def findRootTask(self, id):
        """查找Root任务
        
        参数:
            id:     任务Id
        """
        return self.tasks.findRootTask(id)

    def findTask(self, id):
        """查找任务
        
        参数:
            id:     任务Id
        """
        return self.tasks.findTask(id)

    def getNodeNum(self):
        """节点数量
        """
        return len(self.tasks.tasks)

    def getEdgeNum(self):
        """边数量
        """
        n = 0
        for t in self.tasks.tasks:
            n += len(t.childs.tasks)

        return n

    # 广度遍历
    def BreadthFirstSearch(self):
        def BFS(self, i):
            print(i)
            visited[i] = 1
            for k in range(self.getNodeNum()):
                if self.map[i][k] == 1 and visited[k] == 0:
                    BFS(self, k)

        visited = [0] * self.getNodeNum()
        for i in range(self.getNodeNum()):
            if visited[i] is 0:
                BFS(self, i)

    # 深度遍历
    def DepthFirstSearch(self):
        def DFS(self, i, queue):

            queue.append(i)
            print(i)
            visited[i] = 1
            if len(queue) != 0:
                w = queue.pop()
                for k in range(self.getNodeNum()):
                    if self.map[w][k] is 1 and visited[k] is 0:
                        DFS(self, k, queue)

        visited = [0] * self.getNodeNum()
        queue = []
        for i in range(self.getNodeNum()):
            if visited[i] is 0:
                DFS(self, i, queue)

    def clone(self):
        g = nodeAdjMatrix()
        g.tasksIndex = self.tasksIndex.copy()
        g.rTask = self.rTask.copy()
        g.tTask = self.tTask.copy()
        g.tasks = self.tasks.clone()
        g.path = []
        g.nodenum = self.nodenum
        g.edgenum = self.edgenum
        g.map = []
        g.file = self.file
        g.lastOccurTime = self.lastOccurTime
        return g

    '''
    打印
    '''

    # 输出
    def printGraph(self):
        print("\t-Task Number:<%u>, Edge Number:<%u>" %
              (self.nodenum, self.edgenum))
        self.printMap()

    def printTasks(self, type):
        print('\t-Tasks Id Index: ')
        print(self.tasksIndex)
        print('\t-All Tasks: ')
        self.tasks.printer(type)

    def printMap(self):
        """打印邻接矩阵信息
        """
        print('\t-Matrix:')
        for r in self.map:
            s = '|\t'
            for c in r:
                s = s + str(c) + '\t'
            s = s + '|'
            print(s)

    def printPath(self):
        """打印全部路径
        """
        print('\t-All Paths:' + str(len(self.path)))
        for p in self.path:
            print(p)

    '''
    暂时不实现
    '''

    def insertNode(self, t):
        #        for i in range(self.nodenum):
        #            self.map[i].append(0)
        #
        #        self.nodenum = self.nodenum + 1
        #        ls = [0] * self.nodenum
        #        self.map.append(ls)
        #
        #        print(self.map)
        pass

    # 假删除，只是归零而已
    def deleteNode(self, x):
        #        for i in range(self.nodenum):
        #            if self.map[i][x] is 1:
        #                self.map[i][x] = 0
        #                self.edgenum = self.edgenum - 1
        #            if self.map[x][i] is 1:
        #                self.map[x][i] = 0
        #                self.edgenum = self.edgenum - 1
        pass
