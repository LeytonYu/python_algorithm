'''
功能：解决最短路径问题的经典Bellman-Ford算法
注意事项：最短路径不唯一，可以多次处理同一个顶点，直到找到最短路径，可以处理负权重、负权重环，
但是负权重环必须是独立的，即起点S可达的顶点V的路径上的某个顶点不存在负权重环。
因为“在负权重环存在的路径之下，最短路径问题是没有意义的”
同理：当求解最长路径时，“在正权重环存在的路径之下，最长路径问题是没有意义的”
除非你对路径经过环的次数进行条件限制
'''

from collections import deque
import math

inf = math.inf
print(inf > 0)


# print(None >2)

class BellmanFordSP(object):
    def __init__(self, Graph, s):
        '''
        :param Graph: 有向图的邻接矩阵
        :param s:  起点Start
        '''
        self.Graph = Graph
        self.edgeTo = []  # 用来存储路径结束的横切边（即最短路径的最后一条边的两个顶点）
        self.distTo = []  # 用来存储到每个顶点的最短路径
        self.s = s  # 起点start

    # 打印顶点S到某一点的最短路径
    def PrintPath(self, end):
        path = [end]
        while self.edgeTo[end] != None:
            path.insert(0, self.edgeTo[end])  # 倒排序
            end = self.edgeTo[end]
        return path

    # 路径中含有正（负）权重环判定，即是判断当前顶点是否存在于一个环中。
    def cycle_assert(self, vote):
        '''
        思路：利用顶点出度、入度，当前顶点满足环的“必要条件”是至少1出度、1入度。
        再判断进行看是否起点能否回到起点的路径判断。两项满足则为环。
        '''
        path = [vote]
        while self.edgeTo[vote] != None:
            path.insert(0, self.edgeTo[vote])
            vote = self.edgeTo[vote]
            if path[0] == path[-1]:
                break

        print(path)
        if path[0] == path[-1]:
            return True
        else:
            return False

    # 主程序
    def bellmanford(self):
        d = deque()  # 导入优先队列（队列性质：先入先出）
        for i in range(len(self.Graph[0])):  # 初始化横切边与最短路径-“树”
            self.distTo.append(inf)
            self.edgeTo.append(None)
        self.distTo[self.s] = 0  # 将顶点s加入distTo中
        # print(self.edgeTo,self.distTo)
        count = 0  # 计数标志
        d.append(self.Graph[self.s].index(min(self.Graph[self.s])))  # 将直接距离顶点S最近的点加入队列
        for i in self.Graph[self.s]:  # 将除直接距离顶点S的点外的其他顶点加入队列
            if i != inf and count not in d:
                d.append(count)
            count += 1
        for j in d:  # 处理刚加入队列的顶点
            self.edgeTo[j] = self.s
            self.distTo[j] = self.Graph[self.s][j]
        # print(d,self.edgeTo,self.distTo)
        # print(d)
        while d:
            count = 0
            vote = d.popleft()  # 弹出将该点作为顶点S，重复操作，直到队列为空
            for i in self.Graph[vote]:  # 进行边的松弛技术
                if i != inf and i > 0 and self.distTo[vote] + i < self.distTo[count]:
                    self.edgeTo[count] = vote
                    self.distTo[count] = self.distTo[vote] + i
                    self.distTo[count] = round(self.distTo[count], 2)
                    if count not in d:
                        d.append(count)

                # 处理满足条件且含有正（负）权重环的路径情况
                elif i != inf and i < 0 and self.distTo[vote] + i < self.distTo[count]:
                    temp = self.edgeTo[count]  # 建立临时空间存储原横切边
                    # print(vote,count)
                    self.edgeTo[count] = vote
                    flage = self.cycle_assert(count)  # 判读若该点构成环切该点即是起点有事终点，则存在环
                    if flage:  # 有环，消除该环
                        self.edgeTo[count] = temp
                        self.Graph[vote][count] = inf
                    else:  # 无环，与第一个if相同处理
                        self.distTo[count] = self.distTo[vote] + i
                        self.distTo[count] = round(self.distTo[count], 2)
                        if count not in d:
                            d.append(count)

                elif i != inf and self.distTo[vote] + i >= self.distTo[count]:
                    self.Graph[vote][count] = inf  # 删除该无用边
                    # if count not in d:
                    # d.append(count)
                count += 1
            # print(d)

        # print(self.edgeTo,self.distTo)
        for i in range(len(self.Graph[0])):
            path = self.PrintPath(i)
            print("%d to %d(%.2f)：" % (path[0], i, self.distTo[i]), end="")
            if len(path) == 1 and path[0] == self.s:
                print("")
            else:
                for i in path[:-1]:
                    print('%d->' % (i), end="")
                print(path[-1])


if __name__ == "__main__":
    # 含有负权重值的图
    Graph = [[inf, inf, 0.26, inf, 0.38, inf, inf, inf],
             [inf, inf, inf, 0.29, inf, inf, inf, inf],
             [inf, inf, inf, inf, inf, inf, inf, 0.34],
             [inf, inf, inf, inf, inf, inf, 0.52, inf],
             [inf, inf, inf, inf, inf, 0.35, inf, 0.37],
             [inf, 0.32, inf, inf, 0.35, inf, inf, 0.28],
             # [0.58,inf,0.40,inf,0.93,inf,inf,inf],
             [-1.40, inf, -1.20, inf, -1.25, inf, inf, inf],
             [inf, inf, inf, 0.39, inf, 0.28, inf, inf],
             ]
    # 路径之中含有负权重环图
    Graph1 = [[inf, inf, 0.26, inf, 0.38, inf, inf, inf],
              [inf, inf, inf, 0.29, inf, inf, inf, inf],
              [inf, inf, inf, inf, inf, inf, inf, 0.34],
              [inf, inf, inf, inf, inf, inf, 0.52, inf],
              [inf, inf, inf, inf, inf, 0.35, inf, 0.37],
              [inf, 0.32, inf, inf, -0.66, inf, inf, 0.28],
              [0.58, inf, 0.40, inf, 0.93, inf, inf, inf],
              [inf, inf, inf, 0.39, inf, 0.28, inf, inf],
              ]

    Graph2 = [[inf, 0, 5, inf, inf, inf],
              [inf, inf, inf, 30, 35, inf],
              [inf, inf, inf, 15, 20, inf],
              [inf, inf, inf, inf, inf, 20],
              [inf, inf, inf, inf, inf, 10],
              [inf, inf, inf, inf, inf, inf],
              ]

    Graph3 = [[inf, 0, 5, inf],
              [inf, inf, inf, 35],
              [inf, -7, inf, inf],
              [inf, inf, inf, inf]]

    F = BellmanFordSP(Graph, 0)
    F.bellmanford()
