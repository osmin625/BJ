import sys
from collections import deque
input = sys.stdin.readline
dir = [(0,1),(1,0),(0,-1),(-1,0)]
N,M = map(int,input().split())
grid = [list(map(int,list(input().rstrip()))) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
# 위치, 벽 부순 상태로 방문 여부 확인
# print(*grid,sep='\n')
def bfs():
    m = 1
    q = deque([(0,0,0)])# i,j,벽 부숨 여부
    while q:
        for _ in range(len(q)):
            a,b,w = q.popleft()
            if visited[a][b][w]:
                continue
            visited[a][b][w] = 1
            if (a,b) == (N-1,M-1):
                return m
            for da,db in dir:
                if 0 <= a + da < N and 0 <= b + db < M:
                    if not visited[a + da][b + db][w]:
                        if not grid[a + da][b + db]:
                            q.append((a + da,b + db,w))
                        elif not w:
                            q.append((a + da, b + db, 1))
        m += 1
    return -1
print(bfs())