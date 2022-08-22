import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
# print(grid)
maximum = 0
v = 1

def bfs(x, y):
    q = deque([(x, y, grid[x][y])])
    l = t = 0
    while q and l < 4:
        a, b, c = q.popleft()
        t += c
        visited[a][b] = v
        for da, db in dir:
            if 0 <= a + da < N and 0 <= b + db < M:
                if not visited[a + da][b + db] == v and (a + da, b + db, grid[a + da][b + db]) not in q:
                    q.append((a + da, b + db, grid[a + da][b + db]))
        q = deque(sorted(q, key=lambda x: x[2], reverse=True))
        # print(q, l, t)
        l += 1
    return t

t1 = t2 = t3 = 0
for i in range(N):
    for j in range(M):
        t1 = bfs(i, j)
        if i > 2:
            t2 = grid[i-3][j] + grid[i-2][j] + grid[i-1][j] + grid[i][j]
        if j > 2:
            t3 = grid[i][j-3] + grid[i][j-2] + grid[i][j-1] + grid[i][j]
        # print(temp)
        maximum = sorted([maximum,t1,t2,t3])[3]
        v += 1
print(maximum)
