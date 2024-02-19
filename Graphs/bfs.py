"""
By João Assalim

Breadth First Search:


"""

def bfs(x):
    queue = [x]
    marked = []

    while queue:
        v = queue.pop(0)
        if not v in marked:
            marked.append(v)
            for w in graph[v]:
                if not w in marked:
                    queue.append(w)
    
    print(marked)


n, m = list(map(int, input().split()))

graph = [[] for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

bfs(0)