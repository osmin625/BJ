import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def spread():
    global grid
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] >= 5:
                for di, dj in dir:
                    ci = i + di
                    cj = j + dj
                    if 0 <= ci < R and 0 <= cj < C:
                        if grid[ci][cj] != -1:
                            temp[ci][cj] += grid[i][j] // 5
                            temp[i][j] -= grid[i][j] // 5
    grid = [[grid[i][j] + temp[i][j] for j in range(C)] for i in range(R)]


def cycle():
    for i in reversed(range(0, air_cleaner - 2)):  # 왼쪽위
        grid[i + 1][0] = grid[i][0]
    for i in range(air_cleaner + 2, R):  # 왼쪽아래
        grid[i - 1][0] = grid[i][0]
    for j in range(0, C - 1):
        grid[0][j] = grid[0][j + 1]  # 위
        grid[R - 1][j] = grid[R - 1][j + 1]  # 아래
    for i in range(1, air_cleaner):  # 오른쪽 위
        grid[i - 1][C - 1] = grid[i][C - 1]
    for i in reversed(range(air_cleaner, R - 1)):  # 오른쪽 아래
        grid[i + 1][C - 1] = grid[i][C - 1]
    for j in reversed(range(1, C - 1)):
        grid[air_cleaner - 1][j + 1] = grid[air_cleaner - 1][j]
        grid[air_cleaner][j + 1] = grid[air_cleaner][j]
    grid[air_cleaner][1] = 0
    grid[air_cleaner - 1][1] = 0


def dust_sum():
    dust = 2
    for i in range(R):
        for j in range(C):
            dust += grid[i][j]
    return dust


for i in range(R):
    if grid[i][0] == -1:
        air_cleaner = i + 1
        break

for _ in range(T):
    spread()
    cycle()
print(dust_sum())
