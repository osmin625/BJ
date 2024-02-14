# bfs 문제.
from collections import deque
visited = [[0 for _ in range(500)] for _ in range(500)]
def solution(land):
    n, m = len(land), len(land[0])
    oil = {i:[] for i in range(m)}
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                a,b, sum_ = bfs(land, i,j)
                for idx in range(a,b + 1):
                    oil[idx].append(sum_)
                
                
    print(oil)
    answer = max([sum(oil[i]) for i in range(m)])
    return answer

def bfs(land, i, j):
    dir_ = {(0,1),(0,-1),(1,0),(-1,0)}
    q = deque([[i,j]])
    visited[i][j] = 1
    min_, max_, sum_ = j, j, 0
    n, m = len(land), len(land[0])
    while q:
        x, y = q.popleft()
        max_ = max(y, max_)
        min_ = min(y, min_)
        sum_ += 1
        for dx, dy in dir_:
            if 0 <= x + dx < n and 0 <= y + dy < m:
                if not visited[x + dx][y + dy]:
                    if land[x + dx][y + dy]:
                        visited[x + dx][y + dy] = 1
                        q.append([x + dx, y + dy])
    return min_, max_, sum_