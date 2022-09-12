import sys

input = sys.stdin.readline

V = int(input())
tree = {i: [] for i in range(1, V + 1)}
for _ in range(V):
    temp = list(map(int, input().split()))
    v1 = temp[0]
    for i in range(1, len(temp) - 1, 2):
        tree[v1].append((temp[i], temp[i + 1]))


# print(tree)

def dfs(s):
    visited[s] = 1
    for v, d in tree[s]:
        if not visited[v]:
            dist[v] = dist[s] + d
            dfs(v)


dist = [0 for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]
dfs(1)
s = dist.index(max(dist))
dist = [0 for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]
dfs(s)
print(max(dist))
