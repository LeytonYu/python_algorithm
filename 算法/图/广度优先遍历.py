def bfs(graph,start):
    explored,queue=[],[start]
    explored.append(start)
    while queue:
        v=queue.pop(0)
        for i in graph[v]:
            if i not in explored:
                explored.append(i)
                queue.append(i)
    return explored

G = {'0': ['1', '2'],
     '1': ['2', '3'],
     '2': ['3', '5'],
     '3': ['4'],
     '4': [],
     '5': []}

print(bfs(G, '0'))
