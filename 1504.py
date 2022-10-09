import sys
import heapq

input = sys.stdin.readline


def dijkstra(s):
    dist = [float('inf') for _ in range(N + 1)]
    dist[s] = 0
    q = [(dist[s],s)]
    while q:
        d_sn,n = heapq.heappop(q)
        if d_sn > dist[n]:
            continue
        for d_nc, c in graph[n]:
            d_sc = d_sn + d_nc
            if d_sc < dist[c]:
                dist[c] = d_sc
                heapq.heappush(q,(d_sc,c))
    return dist

N, E = map(int, input().split())
graph = {i:[] for i in range(1,N+1)}
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
v1,v2 = map(int,input().split())
result = min(dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[N], dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[N])
if result > 200000 * 1000:
    result = -1
print(result)