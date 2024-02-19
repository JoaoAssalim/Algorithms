def dfs(x):
    marked[x] = True
    print(x, end=" ")

    for w in graph[x]:
        if not marked[w]:
            dfs(w)


n, m = list(map(int, input().split()))
graph = [[] for i in range(n)]
marked = [False for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

dfs(0)