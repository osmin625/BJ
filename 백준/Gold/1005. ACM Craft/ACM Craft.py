import sys
from collections import deque
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    D = list(map(int,input().split()))
    graph = [[] for i in range(N+1)]
    time = [0 for _ in range(N + 1)]
    ind = [0 for _ in range(N+1)]
    for _ in range(K):
        X,Y = map(int,input().split())
        # 이전 건물을 추적해야 할까, 다음 건물을 추적해야 할까?
        # 다음 건물을 추적하는 방식으로 데이터를 구성한 후,
        # 그래프로 건물을 접근하여 시간을 누적합한다.
        graph[X].append(Y)
        ind[Y] += 1
    q = deque([i for i in range(1,N+1) if not ind[i]])
    for i in q:
        time[i] += D[i-1]
    while q:
        n = q.popleft()
        # time[n] += D[n-1]
        for a in graph[n]:
            ind[a] -= 1
            time[a] = max(time[a], time[n] + D[a - 1])
            if not ind[a]:
                # time[a] += max(parent)
                q.append(a)

    W = int(input())
    print(time[W])