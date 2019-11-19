def dfs(G,s,S=None,res=None):
    if S is None:
        S=set()
    if res is None:
        res=[]
    S.add(s)
    res.append(s)
    for i in G[s]:
        if i in S:
            continue
        S.add(i)
        dfs(G,i,S,res)
    return res

G = {'0': ['1', '2'],
     '1': ['2', '3'],
     '2': ['3', '5'],
     '3': ['4'],
     '4': [],
     '5': []}

print(dfs(G, '0'))