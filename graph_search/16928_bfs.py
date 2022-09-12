import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ls = [0 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    ls[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    ls[u] = v

def bfs():
    cnt = 0
    q = deque([1])
    while q:
        # print(cnt)
        for _ in range(len(q)):
            p = q.popleft()
            # print(q)
            if p == 100:
                return cnt
            for i in range(p + 1, p + 7):
                if i > 100: break
                if not ls[i]:
                    if i not in q:
                        q.append(i)
                elif ls[i] not in q:
                    q.append(ls[i])
        cnt += 1
    return cnt
print(bfs())
