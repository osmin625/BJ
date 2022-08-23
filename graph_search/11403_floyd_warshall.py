import sys
input = sys.stdin.readline

INF = 5
N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]

def fw():
    for i in range(N):
        for j in range(N):
            if not g[i][j]:
                g[i][j] = INF
    for v in range(N): # 경유노드
        for i in range(N): # 출발노드
            for j in range(N): # 도착노드
                if g[i][j] > g[i][v] + g[v][j]:
                    g[i][j] = 1
    for i in range(N):
        for j in range(N):
            if g[i][j] == INF:
                g[i][j] = 0
fw()
for i in range(N):
    print(*g[i])