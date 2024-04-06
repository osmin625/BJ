def bfs(x, y, d):
    ans = 0
    while True:
        # temp = grid[x][y]
        # grid[x][y] = 5
        # print(x, y)
        # print(*grid, sep='\n')
        # grid[x][y] = temp
        if not grid[x][y]:
            grid[x][y] = 2
            ans += 1
        if all([grid[x + dx][y + dy] for dx, dy in dir_.values()]):
            x -= dir_[d][0]
            y -= dir_[d][1]
            if grid[x][y] == 1:
                break
        else:
            d = (d + 1) % 4
            while grid[x + dir_[d][0]][y + dir_[d][1]]:
                d = (d + 1) % 4
            x += dir_[d][0]
            y += dir_[d][1]
    return ans

N, M = map(int,input().split())
r, c, d = map(int,input().split()) # 청소기 위치, 청소기 방향
if d == 1:
    d = 3
elif d == 3:
    d = 1

grid = [list(map(int,input().split())) for _ in range(N)]
dir_ = {0:(-1, 0), 1:(0, -1), 2:(1, 0), 3:(0, 1)} # 북 서 남 동
print(bfs(r, c, d))