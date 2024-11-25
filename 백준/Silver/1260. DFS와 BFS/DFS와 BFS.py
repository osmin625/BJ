from collections import deque

N, M, V = map(int, input().split())
visited = [0] * (N + 1)
graph = {i: [] for i in range(N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = {k: sorted(v) for k, v in graph.items()}


def dfs(n):
    print(n, end=' ')
    visited[n] = 1
    for c in graph[n]:
        if not visited[c]:
            dfs(c)


def bfs(n):
    q = deque([n])
    visited[n] = 1
    print(n, end=' ')
    while q:
        t = q.popleft()
        for c in graph[t]:
            if not visited[c]:
                q.append(c)
                visited[c] = 1
                print(c, end=' ')


dfs(V)
visited = [0] * (N + 1)
print()
bfs(V)
