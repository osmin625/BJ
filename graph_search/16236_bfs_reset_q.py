import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
v = 1
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
fish = []
shark = [2, 0]
q = deque([])
def bfs():
    global q, fish, v
    move = 0
    while q:
        # print(*visited,sep='\n')
        for _ in range(len(q)):
            # print(q)
            x, y, m = q.popleft()
            visited[x][y] = v
            if 0 < grid[x][y] < shark[0]:
                move = m
                grid[x][y] = 0
                # print(shark,'@@@@@',q,x,y,m,'@@@@@@@@@@@@@@@')
                q = deque([])
                fish.pop()
                shark[1] += 1
                if shark[1] == shark[0]:
                    shark[0] += 1
                    shark[1] = 0
                # print(q, (x,y),shark, fish)
                if not fish:
                    return m
                elif fish[-1] >= shark[0]:
                    return m
                v += 1
            for dx, dy in dir:
                if 0 <= x + dx < N and 0 <= y + dy < N:
                    if not visited[x + dx][y + dy] == v:
                        if grid[x + dx][y + dy] <= shark[0] and (x + dx, y + dy, m + 1) not in q:
                            q.append((x + dx, y + dy, m + 1))
            q = deque(sorted(q, key=lambda x: (x[2], x[0], x[1])))
    return move
for i in range(N):
    for j in range(N):
        if 0 < grid[i][j] < 7:
            fish.append(grid[i][j])
        elif grid[i][j] == 9:
            grid[i][j] = 0
            q.append((i, j, 0))
fish = sorted(fish, reverse=True)
result = bfs()
if result == None:
    print(0)
else:
    print(result)
