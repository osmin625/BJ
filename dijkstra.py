import heapq

graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


def dijkstra(g, s):  # g: graph, s: start node
    dist = {d: float('inf') for d in g}  # 모든 간선은 무한대로 초기화
    dist[s] = 0  # s에서 s 까지의 거리는 0
    pq = [(dist[s], s)]  # priority queue --> 간선비용 작은 노드가 우선.
    while pq:
        print(dist)
        d_sn, n = heapq.heappop(pq)   # distance s -> n, 노드 n
        if dist[n] < d_sn:    # s부터 n 까지의 기존 거리보다 크다면 skip
            continue          # dist[s]는 0이기 때문에, 바로 skip
        for c, d_nc in g[n].items():  # 노드 n와 연결된 모든 노드 c에 대하여
            d_sc = d_sn + d_nc  # c 까지의 거리 = n 까지의 거리 + n에서 c 까지의 거리
            if d_sc < dist[c]:  # 기존 거리보다 작으면 갱신
                dist[c] = d_sc
                heapq.heappush(pq, (d_sc, c))  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    return dist

print(dijkstra(graph, 'A'))
