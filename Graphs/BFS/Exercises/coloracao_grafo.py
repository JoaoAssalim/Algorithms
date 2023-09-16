#https://www.beecrowd.com.br/judge/pt/problems/view/1907

def floodFill(img, row, col, p):
    start = img[row][col]
    queue = [(row, col)]
    visited = set()

    while len(queue) > 0:
        row, col = queue.pop(0)
        visited.add((row, col))
        vis[row][col] = True
        img[row][col] = p

        for row, col in neighbors(img, row, col, start):
            if (row, col) not in visited:
                queue.append((row, col))
    
    return img

def neighbors(img, row, col, start):
    indices = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    return [(row, col) for row, col in indices if isValid(img, row, col) and img[row][col] == start]

def isValid(img, row, col):
    return row >= 0 and col >= 0 and row < len(img) and col < len(img[0])


a, b = list(map(int, input().split()))
graph = []

for i in range(a):
    l = list(input())
    graph.append(l)
    
vis = [[False for i in range(b)] for j in range(a)]
c = 0

x, y = 0, 0

while True:
    if x == b:
        x = 0
        y += 1
    
    if y == a:
        break

    if graph[y][x] == '.' and not vis[y][x]:
        floodFill(graph, y, x, 1)
        c += 1
    
    x += 1


print(c)