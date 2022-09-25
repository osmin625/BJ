import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
grid = [[n * 15 for _ in range(n+1)] for _ in range(n+1)]
item = list(map(int, input().split()))
# print(item)

for _ in range(r):
    a, b, l = map(int, input().split())
    grid[a][b] = l
    grid[b][a] = l

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            grid[i][j] = min(grid[i][j],grid[i][k] + grid[k][j])

max_cnt = 0
for i in range(1,n+1):
    grid[i][i] = 0
    cnt = 0
    for j in range(1,n+1):
        if grid[i][j] <= m:
            cnt += item[j-1]
    max_cnt = max(max_cnt,cnt)
print(max_cnt)
