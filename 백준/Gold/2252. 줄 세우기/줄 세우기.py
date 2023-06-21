import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
ind = [0 for _ in range(N+1)]
q = deque()
ans = []

for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    ind[B] += 1

for i in range(1,N+1):
    if not ind[i]:  # 진입차수가 0이라면
        q.append(i)

while q:
    t = q.popleft()
    ans.append(t)
    for i in graph[t]:
        ind[i] -= 1
        if not ind[i]:
            q.append(i)
print(*ans)