import sys
from collections import deque

input = sys.stdin.readline
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque([])
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]


# print(grid)
def bfs(l, a, b):
    q.append((a, b))
    visited[a][b] = l
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            cx = x + dx
            cy = y + dy
            if 0 <= cx < N and 0 <= cy < N:
                if visited[cx][cy] < l < grid[cx][cy]:
                    visited[cx][cy] = l
                    q.append((cx, cy))


max_area = 1
for l in range(1, 100):
    area = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] < l < grid[i][j]:
                bfs(l, i, j)
                area += 1
    max_area = max(max_area, area)
print(max_area)
