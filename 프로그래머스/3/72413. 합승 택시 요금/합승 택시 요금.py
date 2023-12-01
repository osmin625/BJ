# 12: 40
# s -> a 최단거리
# a <-> b 최단거리
# s -> b 최단거리 중 최소값 2개의 합 찾기.
# 다익스트라 3번.
###
# 아니었다.
# 중간에 내리는 경우의 수도 존재한다.
# s -> k -> (k -> a) + (k->b)를 계산.
# 모든 k(a,b,s 포함)에 대해 구한 후 최소를 찾으면 끝.
# 다익스트라가 플로이드 와샬보다 빠른가? 더 빠르다.
import heapq
def dijkstra(graph, s):
    dist = {i:float("inf") for i in graph}
    dist[s] = 0
    pq = [(dist[s], s)]
    while pq:
        d_sn, n = heapq.heappop(pq)
        if dist[n] >= d_sn:
            for d_nc, c in graph[n]:
                d_sc = d_sn + d_nc
                if d_sc < dist[c]:
                    dist[c] = d_sc
                    heapq.heappush(pq,(d_sc, c))
    return dist


def init_graph(n, fares):
    g = {i:[] for i in range(1,n+1)}
    for f in fares:
        n1, n2 ,c = f
        g[n1].append([c,n2])
        g[n2].append([c,n1])
    return g


def solution(n, s, a, b, fares):
    '''
    n : 지점 개수
    s, a, b : 노드 번호
    fares : 2차원 배열
    '''
    answer = []
    graph = init_graph(n,fares)
    dist_s = dijkstra(graph, s)
    for k in graph:
        dist_k = dijkstra(graph, k)
        answer.append(dist_s[k] + dist_k[a] + dist_k[b])
    return min(answer)
    