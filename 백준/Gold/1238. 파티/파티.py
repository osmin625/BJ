import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().rstrip().split())
graph = {i: [] for i in range(1,N+1)}
# print(graph)
for i in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))


def dijkstra(x):
    dist = {d: float('inf') for d in graph}
    dist[x] = 0
    pq = [(dist[x],x)]
    while pq:
        d_xn, n = heapq.heappop(pq)
        if dist[n] < d_xn:
            continue
        for d_nc,c in graph[n]:
            d_xc = d_xn + d_nc
            if d_xc < dist[c]:
                dist[c] = d_xc
                heapq.heappush(pq,(d_xc,c))
    return dist
dist_x = dijkstra(X)
dist = [dijkstra(i)[X] + dist_x[i] for i in range(1,N+1)]
print(max(dist))