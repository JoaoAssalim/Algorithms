def dfs(x, y, stack=[]):
    marked[x] = True
    stack.append(x)
    if x == y:
        print(stack)
        return

    for w in graph[x]:
        if not marked[w]:
            dfs(w, y, stack)
    
    del stack[-1]

n, m = list(map(int, input().split()))
graph = [[] for i in range(n+1)]
marked = [False for i in range(n+1)]

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

dfs(4, 8)