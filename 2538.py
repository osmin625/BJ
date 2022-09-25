import sys
from collections import deque

input = sys.stdin.readline

dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cheese = deque([])
air = [[0 for _ in range(M)] for _ in range(N)]


def air_spread(t):
    air_q = deque([t])
    while air_q:
        x, y = air_q.popleft()
        if air[x][y]:
            continue
        air[x][y] = 1
        for dx, dy in dir:
            cx = x + dx
            cy = y + dy
            if 0 <= cx < N and 0 <= cy < M:
                if not air[cx][cy] and not grid[cx][cy]:
                    air_q.append((cx, cy))


def melt():
    time = 0
    temp = []
    while len(cheese) > 1:
        x, y = cheese.popleft()
        if x == -1 and y == -1:
            cheese.append((-1,-1))
            for a,b in temp:
                grid[a][b] = 0
                air_spread((a, b))
            time += 1
            continue
        air_dir = 0
        for dx, dy in dir:
            cx = x + dx
            cy = y + dy
            if 0 <= cx < N and 0 <= cy < M:
                if air[cx][cy]:
                    air_dir += 1
        if air_dir > 1:
            temp.append((x,y))
            continue
        cheese.append((x, y))
    return time + 1


for i in range(N):
    for j in range(M):
        if grid[i][j]:
            cheese.append((i, j))
cheese.append((-1,-1))
air_spread((0,0))
print(melt())