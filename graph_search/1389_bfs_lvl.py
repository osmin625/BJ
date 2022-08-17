import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().split())
kb = {i:0 for i in range(1,N+1)}
relation = {i:[] for i in range(1,N+1)}
def bfs(s):
    level = 0
    q = deque([s])
    visited[s] = 1
    while q:
        for _ in range(len(q)):
            p = q.popleft()
            for f in relation[p]:
                if not visited[f]:
                    q.append(f)
                    visited[f] = 1
            kb[s] += level
        level += 1
for _ in range(M):
    p1, p2 = map(int,input().split())
    relation[p1].append(p2)
    relation[p2].append(p1)
# print(*relation.items(),sep='\n')
for i in range(1,N+1):
    visited = [0 for _ in range(N + 1)]
    bfs(i)
# print(sorted(kb.items(),key=lambda x:(x[1],x[0])))
print(min(kb.items(),key=lambda x:(x[1],x[0]))[0])