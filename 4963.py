import sys
from collections import deque
input = sys.stdin.readline

dir = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
def bfs(a,b):
    q = deque([(a,b)])
    visited[a][b] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in dir:
            cx = x + dx
            cy = y + dy
            if 0 <= cx < h and 0 <= cy < w:
                if grid[cx][cy]:
                    if not visited[cx][cy]:
                        q.append((cx,cy))
                        visited[cx][cy] = 1
while True:
    w,h = map(int,input().split())
    cnt = 0
    if not w and not h:
        break
    grid = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]:
                if not visited[i][j]:
                    bfs(i,j)
                    cnt += 1
    print(cnt)
