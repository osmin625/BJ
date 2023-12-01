# 1에서 가장 멀리 떨어진 노드 개수
# 위상 정렬 -> DAG가 아님.
# bfs로 풀자.
from collections import deque

def init_graph(n, edge):
    g = {i:[] for i in range(1,n+1)}
    for a, b in edge:
        g[a].append(b)
        g[b].append(a)
    return g

def bfs(graph, start):
    visited = [0 for _ in range(len(graph) + 1)]
    q = deque([start])
    visited[start] = 1
    while q:
        ans = len(q)
        for i in range(len(q)):
            n = q.popleft()
            for c in graph[n]:
                if not visited[c]:
                    visited[c] = 1
                    q.append(c)
    return ans
    
def solution(n, edge):
    graph = init_graph(n,edge)
    answer = bfs(graph, 1)
    return answer