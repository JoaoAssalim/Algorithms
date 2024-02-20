"""
By João Assalim

Breadth First Search:
    BFS work starting add the first node into a queue and
    add it into visited array, removing it from queue and
    add it all children into queue and repeating it again

    It goes for 'layer'

Time Complexity:
    O(n)

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


n, m = list(map(int, input().split())) # nodes, edges
graph = [[] for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

bfs(0)