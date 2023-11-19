# 1. prim / kruskal
# 2. 가장 비용이 많이 드는 길 제거.
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
edges = []
parent = [i for i in range(N+1)]
for i in range(M):
    A,B,C = map(int,input().split())
    edges.append([C,A,B])
edges.sort(key=lambda x:x[0])

def get_set_parent(x):
    global parent
    if parent[x] == x:
        return x
    parent[x] = get_set_parent(parent[x])
    return parent[x]

def union_parent(n1,n2):
    n1 = get_set_parent(n1)
    n2 = get_set_parent(n2)
    if n1 < n2:
        parent[n2] = n1
    else:
        parent[n1] = n2

ans = 0
max_ = 0
for cost, a, b in edges:
    if get_set_parent(a) != get_set_parent(b):
        union_parent(a, b)
        max_ = max(cost,max_)
        ans += cost
print(ans-max_)