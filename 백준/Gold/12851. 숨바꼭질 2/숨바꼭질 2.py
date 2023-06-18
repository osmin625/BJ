import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split())
m = [0 for _ in range(100001)]
cnt = [0 for _ in range(100001)]
# 순차적인 접근으로는 -1, +1, //2로부터의 접근을 동시에 비교하기 어렵다.
# 그래프 탐색으로 풀어보자.
def bfs():
    q = deque([N])
    cnt[N] = 1
    if N == K:
        return
    while q:
        i = q.popleft()
        for ni in [i-1,i+1,i * 2]:
            if 0 <= ni < 100001:
                if not m[ni]:
                    m[ni] = m[i] + 1
                    cnt[ni] = cnt[i]
                    q.append(ni)
                elif m[ni] == m[i] + 1:
                    cnt[ni] += cnt[i]
bfs()
print(m[K],cnt[K],sep='\n')