# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:15:48 2017

@author: liuning11
"""

from Task import Task
from TaskCollection import TaskCollection
from Graph import Graph


class TaskAdjMatrix(Graph):
    """
    
    tasksIndex  所有节点ID
    tasks       所有节点实例
    rTask       根节点
    tTask       终端节点
    nodenum     节点数量
    edgenum     边数量
    map         邻接矩阵
    path        节点配置文件
    file        节点配置文件
    
    
    
    
    邻接矩阵
    
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
    
    规划时间：
    采用markdown公式 
    
    a_(t_a,d_a)->b_(t_a+d_a,d_b)->c_(t_a+d_a+d_b,d_c)
    a_(t_a,d_a)->b_(t_a+d_a,d_b)->d_(t_a+d_a+d_b,d_d)->e_(t_a+d_a+d_b+d_d,d_e)
    f_(t_f,d_f)->e_(t_f+d_f,d_e)
    
    先标记所有父任务大于1的任务    

    
    
    """

    def __init__(self):
        self.tasksIndex = []
        self.tasks = TaskCollection()
        self.rTask = []
        self.tTask = []
        self.path = []
        self.nodenum = 0
        self.edgenum = 0
        self.map = []
        self.file = None

    # 添加任务ID 
    def addTasksIndex(self, taskId):
        if self.isExistOfTaskIndex(taskId) == False:
            self.tasksIndex.append(taskId)

    # 判断任务Id是否已经存在
    def isExistOfTaskIndex(self, taskId):
        for id in self.tasksIndex:
            if id == taskId:
                return True
        return False

    # 添加任务
    def addTask(self, t):
        self.tasks.add(t)

    # 创建邻接矩阵
    def createMap(self):
        self.__beforeMap()
        self.__goMap()
        self.__afterMap()

    # 初始化邻接矩阵

    def __beforeMap(self):
        for i in range(self.nodenum):
            m = [0] * self.nodenum
            self.map.append(m)

    def __goMap(self):
        self.rTask = [0] * self.nodenum
        self.tTask = [0] * self.nodenum
        for x in self.tasks.tasks:
            for y in x.childs.tasks:
                w = self.__findIndex(x.id)
                v = self.__findIndex(y.id)
                self.addEdge(w, v)

                self.tTask[w] = 1
                self.rTask[v] = 1

    def __afterMap(self):
        for i in range(self.nodenum):
            self.map[i].append(self.tasksIndex[i])

        self.map.append(self.tasksIndex)

    def __findIndex(self, id):
        j = -1
        for i in range(len(self.tasksIndex)):
            if id == self.tasksIndex[i]:
                j = i
                break
        return j

    def isOutRange(self, x):
        try:
            if x >= self.nodenum or x <= 0:
                raise IndexError
        except IndexError:
            print("节点下标出界")

    # 添加边
    def addEdge(self, x, y):
        if self.map[x][y] is 0:
            self.map[x][y] = 1
            self.edgenum = self.edgenum + 1

    # 删除边
    def removeEdge(self, x, y):
        if self.map[x][y] is 0:
            self.map[x][y] = 1
            self.edgenum = self.edgenum + 1

    # 查找邻接矩阵所有的路径
    def searchPath(self):
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

    # 查找指定节点的所有子节点
    def findChildByMatrix(self, id):
        n = []
        r = self.__findIndex(id)
        for i in range(self.getNodeNum()):
            if self.map[r][i] == 1:
                n.append(self.map[r][i])

        return n

    # 查找指定节点的父节点
    def findParentByMatrix(self, id):
        n = []
        r = self.__findIndex(id)
        for i in range(self.getNodeNum()):
            if self.map[i][r] == 1:
                n.append(self.map[i][r])

        return n

    # 根据路径集合检索
    def findPathByStr(self, id):
        l = []
        for p in self.path:
            if '->' + id in p or id + '->' in p:
                l.append(p)
        return l

    # 查找指定节点的行列索引
    def __findIndex(self, id):
        for i in range(len(self.tasksIndex)):
            if id == self.tasksIndex[i]:
                return i

    # 查找任务
    def findRootTask(self, id):
        return self.tasks.findRootTask(id)

    # 查找任务
    def findTask(self, id):
        return self.tasks.findTask(id)
    
    # 是否为路径
    def __isPath(self, path):
        for p in self.path:
            if path in p:
                return True
        return False

    def sort(self):
        pass
    
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

    '''
    打印
    '''

    # 输出
    def printGraph(self):
        self.printSummary()
        self.printTasks()
        self.printMap()
        print('\n')

    # 打印概述信息
    def printSummary(self):
        print("the Number Of Task: ")
        print("\t" + str(self.nodenum))
        print("the Number Of Edge:")
        print("\t" + str(self.edgenum))

    # 打印任务信息    
    def printTasks(self):
        print('Task: ')
        print(self.tasksIndex)
        print('Task List: ')
        self.tasks.printer()
        print('\n')

    def printRootTasks(self):
        print('Task root: ')
        print(self.tasksIndex)
        print('Task List: ')
        for t in self.tasks.tasks:
            print(t.toString(True))
        print('\n')
        
    # 打印邻接矩阵信息
    def printMap(self):
        print('Matrix:')
        for m in self.map:
            print(m)
        print('\n')

    # 打印全部路径
    def printPath(self):
        print('All of Path:' + str(len(self.path)))
        for p in self.path:
            print(p)
        print('\n')

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
