import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[float('inf') for _ in range(0,N+1)] for _ in range(0,N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    # graph[b][a] = 1

def floyd():
    cnt = 0
    for k in range(1,N+1):
        flag = 0
        graph[k][k] = 0
        for i in range(1,N+1):
            for j in range(1,N+1):
                graph[i][j] = min(graph[i][j],graph[i][k] + graph[k][j])
            if k != i and graph[k][i] > M and graph[i][k] > M:
                flag = 1
        if not flag:
           cnt += 1
    return cnt
print(floyd())