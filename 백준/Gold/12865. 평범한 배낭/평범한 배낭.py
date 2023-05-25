import sys
input = sys.stdin.readline
N, K = map(int,input().split())
things = [list(map(int,input().split())) for _ in range(N)]
m = [[0 for _ in range(K+1)] for _ in range(N)]
for i in range(N): # 100
    w = things[i][0]
    v = things[i][1]
    for j in range(K+1): # 100000
        if j < w:
            m[i][j] = m[i-1][j]
        else:
            m[i][j] = max(v + m[i-1][j-w], m[i-1][j])
print(m[N-1][K])
