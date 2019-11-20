from queue import Queue
import numpy as np
import math

inf = math.inf
npa = np.array
npm = np.mat


def spfa(s, node=0, inf=np.inf, method='simple'):
    """
    单源最短路的SPFA算法，Shortest Path Faster Algorithm
    :param s:距离矩阵（邻接矩阵表示）其中s[i][j]代表i到j的距离
    :param node:源点
    :param inf:无穷大值
    :param method:
    'simple':简单算法，针对非负距离（注意不是非负环）有效
    :return:
    """
    if method == 'simple':
        return _spfa_simple(s, node, inf)
    elif method == 'cut':
        return _spfa_cut(s, node, inf)
    else:
        raise ValueError("method not found")


def _spfa_simple(s, node=0, inf=np.inf):
    """
    单源最短路径算法，
    只对非负权值有效
    :param s: 距离矩阵（邻接矩阵表示）其中s[i][j]代表i到j的距离
    :param node:源点
    :return:
    """
    a = npa(s)
    m, n = a.shape
    if m != n:
        raise ValueError("s 需要是方阵")
    dis = np.ones(n) * inf
    print(dis)
    vis = np.zeros(n, dtype=np.int8)
    dis[node] = 0
    vis[node] = 1
    que = Queue()
    prenode = -np.ones(n, dtype=np.int8)  # 记录前驱节点，没有则用-1表示
    que.put(node)
    while not que.empty():
        v = que.get()
        vis[v] = 0
        for i in range(n):
            temp = dis[v] + a[v][i]
            if a[v][i] > 0 and dis[i] > temp:
                dis[i] = temp  # 修改最短路
                prenode[i] = v
                if vis[i] == 0:  # 如果扩展节点i不在队列中，入队
                    que.put(i)
                    vis[i] = 1
    return dis, prenode


def _spfa_cut(s, node=0, inf=np.inf):
    """
    单源最短路径算法，
    只对非负环有效
    :param s: 距离矩阵（邻接矩阵表示）其中s[i][j]代表i到j的距离
    :param node:源点
    :return:
    """
    a = npa(s)
    m, n = a.shape
    if m != n:
        raise ValueError("s 需要是方阵")
    count = np.zeros(n, dtype=np.int8)
    dis = np.ones(n) * inf
    vis = np.zeros(n, dtype=np.int8)
    dis[node] = 0
    vis[node] = 1
    que = Queue()
    prenode = -np.ones(n, dtype=np.int8)  # 记录前驱节点，没有则用-1表示
    que.put(node)
    while not que.empty():
        v = que.get()
        vis[v] = 0
        for i in range(n):
            temp = dis[v] + a[v][i]
            if dis[i] > temp:
                dis[i] = temp  # 修改最短路
                prenode[i] = v
                if vis[i] == 0:  # 如果扩展节点i不在队列中，入队
                    count[i] += 1
                    if count[i] > n:
                        raise ValueError("输入有负环异常")
                    que.put(i)
                    vis[i] = 1
    return dis, prenode

