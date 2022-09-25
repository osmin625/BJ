import sys
import heapq
input = sys.stdin.readline

def dijkstra(s):
    dist = [float('inf') for _ in range(n + 1)]
    route = [[] for _ in range(n + 1)]
    dist[s] = 0
    q = [(0, s, [s])]
    while q:
        sv_d, v, l = heapq.heappop(q)
        if sv_d > dist[v]:
            continue
        for vc_d, c in graph[v]:
            sc_d = sv_d + vc_d
            if sc_d < dist[c]:
                dist[c] = sc_d
                route[c] = l + [c]
                heapq.heappush(q, (sc_d, c, l + [c]))
    return dist, route


n = int(input())
m = int(input())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    s, d, w = map(int, input().split())
    graph[s].append([w, d])
start, end = map(int, input().split())
dist, route = dijkstra(start)
print(dist[end])
print(len(route[end]))
print(*route[end])

