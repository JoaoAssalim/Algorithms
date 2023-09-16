def floodFill(img, row, col, p, path):
    start = img[row][col]
    queue = [(row, col)]
    visited = set()
    came_from = {}

    while len(queue) > 0:
        r, c = queue.pop(0)
        visited.add((r, c))
        img[r][c] = p

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(img) and 0 <= nc < len(img[0]) and img[nr][nc] == start and (nr, nc) not in visited:
                queue.append((nr, nc))
                came_from[(nr, nc)] = (r, c)

    if graph[0][0] == graph[4][4]:
        current = (4, 4)
        while current != (0, 0):
            path.insert(0, current)
            current = came_from[current]

    return img, path

for i in range(int(input())):
    graph = []
    
    i = 0
    while i < 5:
        l = list(map(int, input().split()))
        if len(l) > 0:
            graph.append(l)
            i += 1

    vis = [[False for i in range(5)] for j in range(5)]
    path = []

    if graph[0][0] != 1:
        graph, path = floodFill(graph, 0, 0, 3, path)

        if graph[0][0] == graph[4][4]:
            print("COPS")
            for r, c in path:
                print(f"({r}, {c}) -> ", end="")
            print(f"({0}, {0})")
        else:
            print("ROBBERS")
    else:
        print("ROBBERS")
