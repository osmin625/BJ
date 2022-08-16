import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
graph = {i:[] for i in range(1,N+1)}
visited = [0 for _ in range(0,N+1)]
for _ in range(int(input())):
    c1, c2 = map(int,input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)
def bfs():
    computer = 0
    q = deque([1])
    visited[1] = 1
    while q:
        n = q.popleft()
        visited[n] = 1
        for i in graph[n]:
            if not visited[i] and not i in q:
                q.append(i)
                computer += 1
    return computer
print(bfs())