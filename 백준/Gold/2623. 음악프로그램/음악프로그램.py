import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N + 1)]
ind = [0 for _ in range(N+1)]
for _ in range(M):
    n, *singer = map(int, input().split())
    for i in range(n - 1):
        graph[singer[i]].append(singer[i + 1])
        ind[singer[i + 1]] += 1

q = deque([n for n in range(1, N+1) if not ind[n]])
ans = []
while q:
    n = q.popleft()
    ans.append(n)
    for a in graph[n]:
        ind[a] -= 1
        if not ind[a]:
            q.append(a)
if len(ans) < N:
    print(0)
else:
    print(*ans, sep='\n')