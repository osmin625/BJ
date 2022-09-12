import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
md = 0
for _ in range(n-1):
    v1,v2,d = map(int,input().split())
    tree[v1].append((v2,d))
def dfs(v,d):
    global md
    l = r = 0
    for nv, w in tree[v]:
        t = dfs(nv,w)
        if l <= r:
            l = max(l,t)
        else:
            r = max(r,t)
    md = max(md,l + r)
    return d + max(l, r)
dfs(1,0)
print(md)