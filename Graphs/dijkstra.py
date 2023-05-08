import heapq

def dijkstra(G,start):  
    INF = 999999999

    dis = dict((key,INF) for key in G)
    dis[start] = 0
    vis = dict((key,False) for key in G)
    pq = []
    heapq.heappush(pq,[dis[start],start])

    path = dict((key,[start]) for key in G)
    while len(pq)>0:
        v_dis,v = heapq.heappop(pq)
        if vis[v] == True:
            continue
        vis[v] = True
        p = path[v].copy()
        for node in G[v]:
            new_dis = dis[v] + float(G[v][node])
            if new_dis < dis[node] and (not vis[node]):
                dis[node] = new_dis
                heapq.heappush(pq,[dis[node],node])
                temp = p.copy()
                temp.append(node)
                path[node] = temp

    return dis,path
    
V, A = list(map(int, input().split()))
G= {}
for i in range(1, V+1):
    G[i] = {i:0}
    
for i in range(A):
    ini, fim, peso = list(map(int, input().split()))
    G[ini].update({fim:peso})

distance,path = dijkstra(G,1)
