def dfs(x):
    if(vis[x] == 1): 
        return
    vis[x] = 1
    print(x, end=" ")
    
    for i in range(0, len(graph[x])):
        y = graph[x][i]
        if(vis[y] == 0):
            dfs(y)

V, A = list(map(int, input().split()))
graph = [[] for i in range(V+1)]
vis = [0 for i in range(V+1)]

for i in range(A):
    u,v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

dfs(1)