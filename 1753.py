import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = {i: [] for i in range(1, V + 1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))


# print(graph)

def dijkstra(g, s):
    dist = [float('inf') for _ in range(0, V + 1)]
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d_sn, n = heapq.heappop(pq)
        if dist[n] < d_sn:
            continue
        for d_nc, c in g[n]:
            d_sc = d_sn + d_nc
            if d_sc < dist[c]:
                dist[c] = d_sc
                heapq.heappush(pq, (d_sc, c))
    return dist


for i in dijkstra(graph, K)[1:]:
    print(i if i < 200000 else 'INF')
