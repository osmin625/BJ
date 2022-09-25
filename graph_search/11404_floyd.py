import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
grid = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    grid[a][b] = min(grid[a][b], c)
# print(*grid,sep='\n')
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == k or j == k or i == j:
                continue
            grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])
for i in range(1, n + 1):
    grid[i][i] = 0
    for j in range(1, n + 1):
        print(grid[i][j] if grid[i][j] <= 100 * 100000 else 0, end=' ')
    print()
