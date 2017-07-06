# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:15:48 2017

@author: liuning11
"""

from TaskCollection import TaskCollection
from Graph import Graph
import DateTimeUtil


class TaskAdjMatrix(Graph):
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
            tasksIndex  所有节点ID
            tasks       所有节点实例
            rTask       根节点
            tTask       终端节点
            nodenum     节点数量
            edgenum     边数量
            map         邻接矩阵
            path        节点配置文件
            file        节点配置文件
            lastOccurTime    最晚任务时间
        返回:
        异常:
        """
        self.tasksIndex = []
        self.tasks = TaskCollection()
        self.rTask = []
        self.tTask = []
        self.path = []
        self.nodenum = 0
        self.edgenum = 0
        self.map = []
        self.file = None
        self.lastOccurTime = 0.0

    def createMap(self):
        """创建邻接矩阵
        """

        def before(self):
            """初始化邻接矩阵
    
            参数:
            返回:
            异常:
            """

            self.nodenum = self.getNodeNum()
            self.edgenum = self.getEdgeNum()

            for i in range(self.nodenum):
                m = [0] * self.nodenum
                self.map.append(m)

        def create(self):
            """创建邻接矩阵
    
            参数:
            返回:
            异常:
            """
            self.rTask = [0] * self.nodenum
            self.tTask = [0] * self.nodenum
            for x in self.tasks.tasks:
                for y in x.childs.tasks:
                    w = self.__findIndex(x.id)
                    v = self.__findIndex(y.id)
                    self.addEdge(w, v)

                    self.tTask[w] = 1
                    self.rTask[v] = 1

        def after(self):
            """在邻接矩阵行-列追加所有任务ID
    
            参数:
            返回:
            异常:
            """
            for i in range(self.nodenum):
                self.map[i].append(self.tasksIndex[i])

            self.map.append(self.tasksIndex)

        self.map = []
        before(self)
        create(self)
        #after(self)

        if self.config.debug == True:
            print('--Stage Ajd Matrix:')

            self.printGraph()

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

    def addEdge(self, x, y):
        """添加边

        参数:
            x:  row
            y:  column
        返回:
        异常:
        """
        if self.map[x][y] is 0:
            self.map[x][y] = 1

    def removeEdge(self, x, y):
        """删除边

        参数:
            x:  row
            y:  column
        返回:
        异常:
        """
        if self.map[x][y] is 0:
            self.map[x][y] = 1
            self.edgenum = self.edgenum - 1

    def searchPath(self):
        """查找邻接矩阵所有路径

        参数:
        返回:
        异常:
        """

        def path(self, s, r):
            for i in range(self.nodenum):
                if self.map[r][i] == 1:
                    s.append(self.tasksIndex[i])
                    path(self, s, i)
                    s.pop()
                else:
                    if i >= self.nodenum - 1:
                        p = '->'.join(s)
                        if self.__isPath(p) == False:
                            self.path.append(p)

        s = []
        for r in range(len(self.rTask)):
            s.clear()
            if self.rTask[r] == 0:
                s.append(self.tasksIndex[r])
                path(self, s, r)

        if self.config.debug == True:
            self.printPath()

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

    def __isPath(self, path):
        """是否为一个任务路径
        """
        for p in self.path:
            if path in p:
                return True
        return False

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
        g = TaskAdjMatrix()
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
        print('???????????????????????????????????')
        self.printSummary()
        self.printTasks()
        self.printMap()

    # 打印概述信息
    def printSummary(self):
        print("\t-Conf File: <%s>, Task Number:<%u>, Edge Number:<%u>" %
              (self.file, self.nodenum, self.edgenum))

    def printLastOccurTime(self):
        print('\t-Last Time When Task Occur:<%s>' %
              (DateTimeUtil.timestamp_datetime(self.lastOccurTime)))

    # 打印任务信息    
    def printTasks(self):
        self.printTasksIndex()
        print('\t-All Tasks: ')
        self.tasks.printer()

    def printTasksIndex(self):
        """打印任务ID
        """
        print('\t-Tasks Index: ')
        print(self.tasksIndex)

    def printRootTasks(self):
        """打印所有ROOT任务
        """
        print('\t-Root Task: ')
        for t in self.tasks.tasks:
            print(t.toString(True))

    def printMap(self):
        """打印邻接矩阵信息
        """
        print('\t-Matrix:')
        for m in self.map:
            print(m)

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


#    def addTasksIndex(self, taskId):
#        """添加任务ID 
#
#        参数:
#            taskId:  任务Id
#        返回:
#        异常:
#        """
#
#        def isExist(self, taskId):
#            """判断任务Id是否已经存在
#    
#            参数:
#                taskId:  任务Id
#            返回:
#            异常:
#            """
#            for id in self.tasksIndex:
#                if id == taskId:
#                    return True
#            return False
#
#        if isExist(self, taskId) == False:
#            self.tasksIndex.append(taskId)
