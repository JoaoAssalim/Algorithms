def isBipartite(adj, v, visited, color):
    for u in adj[v]:
        if (visited[u] == False):
            visited[u] = True
            color[u] = not color[v]
            if (not isBipartite(adj, u, visited, color)):
                return False

        elif (color[u] == color[v]):
            return False
     
    return True
 
N = 6
adj = [[] for i in range(N + 1)]
visited = [0 for i in range(N + 1)]
color = [0 for i in range(N + 1)]

for i in range(N):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

visited[1] = True
color[1] = 0
if (isBipartite(adj, 1, visited, color)):
    print("Graph is Bipartite")
else:
    print("Graph is not Bipartite")