import sys
import heapq
input = sys.stdin.readline
def dijkstra(s):
    dist = [float('inf') for _ in range(N+1)]
    dist[s] = 0
    q=[(dist[s],s)]
    while q:
        d_sn,n = heapq.heappop(q)
        if d_sn > dist[n]:
            continue
        for d_nc,c in city[n]:
            d_sc = d_sn + d_nc
            if d_sc < dist[c]:
                dist[c] = d_sc
                heapq.heappush(q,(d_sc,c))
    return dist

N = int(input())
M = int(input())
city = {i:[] for i in range(1,N+1)}
for _ in range(M):
    s,d,w = map(int,input().split())
    city[s].append((w,d))
start, end = map(int,input().split())
print(dijkstra(start)[end])