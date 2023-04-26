import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
m = [0 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(i):
        if grid[j][0] <= i-j:
            m[i] = max(m[i], m[j] + grid[j][1])
print(max(m))