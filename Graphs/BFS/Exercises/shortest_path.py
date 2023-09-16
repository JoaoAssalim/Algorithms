def bfs_shortest_path(graph, start):
    queue = [start]
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    visited = set()

    while queue:
        vertex = queue.pop(0)
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
     
    return distances
 
graph = [[1, 2], [2, 3], [3], [4], []]
 
start_vertex = 0
distances = bfs_shortest_path(graph, start_vertex)
 
print(distances)