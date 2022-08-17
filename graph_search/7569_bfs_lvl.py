# 토마토
import sys

input = sys.stdin.readline
from collections import deque

dir = [(0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0)]
M, N, H = map(int, input().split())
day = 0
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque([])

# print(box)

def bfs():
    global day
    temp = 0
    while q:
        for _ in range(len(q)):
            # print(q)
            # print(*box, sep='\n', end='\n\n')
            a, b, c = q.popleft()
            box[a][b][c] = 2
            for x, y, z in dir:
                if 0 <= x + a < H and 0 <= y + b < N and 0 <= z + c < M:
                    if box[x + a][y + b][z + c] == 0:
                        box[x + a][y + b][z + c] = 1
                        q.append((x + a, y + b, z + c))
        temp += 1
    temp -= 1
    if temp > day:
        day = temp

f1 = f2 = 0
for h in range(H):
    for i in range(N):
        if not all(box[h][i]):
            f1 = 1
if f1:
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if box[h][i][j] == 1:
                    q.append((h, i, j))
    bfs()
    for h in range(H):
        for i in range(N):
            if not all(box[h][i]):
                f2 = 1
                break
        if f2:
            break
    if f2:
        print(-1)
    else:
        print(day)
else:
    print(day)