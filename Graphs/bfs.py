def bfs(x):
    q = []
    q.append(x)
    vis[x] = 1
    
    while(len(q) > 0):
        atual = q[0]
        print(atual, end=" ")
        q = q[1:]
        
        for i in range(len(graph[atual])):
            y = graph[atual][i]
            
            if vis[y] == 0:
                q.append(y)
                vis[y] = 1

V, A = list(map(int, input().split()))
graph = [[] for i in range(V+1)]
vis = [0 for i in range(V+1)]

for i in range(A):
    u,v = list(map(int, input().split()))
    graph[u].append(v)

bfs(1)