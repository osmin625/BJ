import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])
parent = [i for i in range(V + 1)]


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


def union_parent(n1, n2):
    n1 = get_parent(n1)
    n2 = get_parent(n2)
    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2


ans = 0
for a, b, cost in edges:
    if get_parent(a) != get_parent(b):
        union_parent(a, b)
        ans += cost
print(ans)
