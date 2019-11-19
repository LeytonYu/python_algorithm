class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [[0] * vertex for i in range(vertex)]

    def insert(self, u, v):
        # 对存在连接关系的两个点，在矩阵里置1代表存在连接关系，没有连接关系则置0
        self.graph[u - 1][v - 1] = 1
        self.graph[v - 1][u - 1] = 1

    def show(self):  # 展示图
        for i in self.graph:
            for j in i:
                print(j, end=' ')
            print(' ')