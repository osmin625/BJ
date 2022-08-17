# 토마토
import sys
from collections import deque
input = sys.stdin.readline

dir = {(0,1),(1,0),(0,-1),(-1,0)}
M,N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]
q = deque([])

def bfs():
    day = 0
    while q:
        for _ in range(len(q)):
            a,b = q.popleft()
            box[a][b] = 2
            for da,db in dir:
                if 0 <= a + da < N and 0 <= b + db < M:
                    if not box[a + da][b + db]:
                        box[a + da][b + db] = 1
                        q.append((a + da,b + db))
        day += 1
    for i in range(N):
        if not all(box[i]):
            return -1
    return day -1

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
print(bfs())