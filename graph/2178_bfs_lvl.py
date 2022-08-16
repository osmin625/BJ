import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
maze = [list(map(int,list(input().rstrip()))) for _ in range(N)]
dir = [(0,1),(1,0),(0,-1),(-1,0)]
# print(*maze,sep='\n')
def bfs():
    way = 1
    q = deque([(0,0)])
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
            for dx, dy in dir:
                if 0 <= x + dx < N and 0 <= y + dy < M:
                    if x + dx == N-1 and y + dy == M-1:
                        return way + 1
                    elif maze[x + dx][y + dy] == 1:
                        maze[x + dx][y + dy] = 2
                        q.append((x + dx, y + dy))
                        # print(q)
                        # print(*maze,sep='\n')
        way += 1
print(bfs())