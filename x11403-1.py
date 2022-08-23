import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
q = deque([])
def bfs():
    stack = []
    while q:
        flag = 0
        a, b = q.popleft()
        visited[a][b] = 1
        if not a in stack:
            stack.append(a)
        for j in range(N):
            if g[b][j] == 1 and not visited[b][j]:
                for s in stack:
                    visited[s][j] = 1
                q.append((b, j))
                flag = 1
        if not flag:
            stack.pop()
        print(stack)
for i in range(N):
    for j in range(N):
        if g[i][j] == 1:
            q.append((i,j))
bfs()
for a in visited:
    print(*a, sep=' ')
