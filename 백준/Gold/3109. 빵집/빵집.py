import sys

input = sys.stdin.readline

R, C = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]

dir_x = [-1, 0, 1]
first, ans = 1, 0

# 경로 추적이 필요한가?
# 성공했을 때 제대로 끝낼 필요가 있다.
def dfs(x, y):
    global R, C, ans, first
    if not first:
        return
    visited[x][y] = 1
    if y == C - 1:
        ans += 1
        first = 0
        return
    for dx in dir_x:
        if 0 <= x + dx < R and y < C - 1:
            if grid[x + dx][y + 1] == '.' and not visited[x + dx][y + 1]:
                dfs(x + dx,y + 1)

for i in range(R):
    dfs(i, 0)
    first = 1
print(ans)
