"""
By João Assalim

Depth First Search:
    It works recursively, you add the x 
    in marked array, and iterate in each
    element in graph[x], and if the element 
    is not in marked array, you call
    dfs recursively.

    It goes deepest as possible

Time Complexity:
    O(n)

"""

def dfs(x, marked=[]):
    marked.append(x)
    print(x, end=" ")

    for w in graph[x]:
        if not w in marked:
            dfs(w, marked)

n, m = list(map(int, input().split())) # nodes, edges
graph = [[] for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

dfs(0)