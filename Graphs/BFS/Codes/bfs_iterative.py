def bfs(x):
    queue = [x]

    while len(queue) > 0:
        v = queue.pop(0)
        print(v, end=" ")
        if not marked[v]:
            marked[v] = True
            for w in graph[v]:
                if not marked[w]:
                    queue.append(w)

            
n, m = list(map(int, input().split()))

graph = [[] for i in range(n)]
marked = [False for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

bfs(0)