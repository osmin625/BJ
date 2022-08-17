import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
relation = {i:[] for i in range(1,n+1)}
visited = [0 for _ in range(n+1)]
p1, p2 = map(int,input().split())
for _ in range(int(input())):
    p,c = map(int,input().split())
    relation[p].append(c)
    relation[c].append(p)
# print(relation)
def bfs(p1,p2):
    chon = 0
    q = deque([p1])
    while q:
        for _ in range(len(q)):
            n = q.popleft()
            visited[n] = 1
            for i in relation[n]:
                if i == p2:
                    return chon + 1
                elif not visited[i] and not i in q:
                    q.append(i)
        chon += 1
c = bfs(p1,p2)
if c:
    print(c)
else:
    print(-1)