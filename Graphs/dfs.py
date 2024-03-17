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

def dfs_iter(x):
    stack = [x]
    visited = []
    
    while stack:
        v = stack.pop()
        if not v in visited:
            visited.append(v)
            for i in graph[v]:
                stack.append(i)
    
    print(visited)


def dfs_rec(x, visited=[]):
    print(x, end=" ")
    visited.append(x)
    
    for v in graph[x]:
        if not v in visited:
            dfs_rec(v, visited)
    

n, m = list(map(int, input().split()))
graph = [[] for i in range(n)]

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

dfs_iter(0)
print()
dfs_rec(0)
