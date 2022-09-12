from collections import deque
N, K = map(int, input().split())
m = [-1 for _ in range(150001)]
ts = [2 ** i for i in range(17)]
# print(ts)
def bfs():
    q = deque([(N,0)])
    while q:
        i,c = q.popleft()
        if m[i] != -1 and m[i] <= c:
            continue
        m[i] = c
        for t in ts:
            if 0 <= i * t < 150000:
                q.append((i * t,c))
        for n in [i + 1, i - 1]:
            if 0 <= n < 150000:
                q.append((n,c + 1))
bfs()
print(m[K])