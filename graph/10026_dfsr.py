import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
pic = [list(input().rstrip()) for _ in range(N)]
visited = [[0 for _ in range(N)]for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
normal = 0
color_blindness = 0
# print(*pic,sep = '\n')
def dfs(status,r, c):
    current = pic[r][c]
    visited[r][c] = 1
    for dx, dy in dir:
        if 0 <= r + dx < N and 0 <= c + dy < N and status == 'n' and not visited[r + dx][c + dy]:
            if pic[r+ dx][c + dy] == current:
                dfs(status,r + dx,c + dy)
        elif 0 <= r + dx < N and 0 <= c + dy < N and status == 'cb' and not visited[r + dx][c + dy]:
            if current == 'B' and pic[r + dx][c + dy] == 'B':
                dfs(status,r + dx,c + dy)
            elif current == 'R' or current == 'G':
                if pic[r + dx][c + dy] == 'G' or pic[r + dx][c + dy] == 'R':
                    dfs(status,r + dx,c + dy)
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs('n',i,j)
            normal += 1
visited = [[0 for _ in range(N)]for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs('cb',i,j)
            color_blindness += 1

print(normal, color_blindness)