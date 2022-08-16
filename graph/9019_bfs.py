# DSLR
import sys
from collections import deque
input = sys.stdin.readline

def bfs(a,b):
    q = deque([(a,-1)])
    while m[b] == -1:
        v, p = q.popleft()
        if m[v] == -1:
            m[v] = p
            q.append(((v * 2)% 10000,v)) #D
            if v:
                q.append((v-1,v)) #S
            else:
                q.append((9999,v))
            q.append(((v % 1000) * 10 + (v // 1000),v))
            q.append(((v % 10) * 1000 + (v // 10),v))
    result = ''
    while b != a:
        if (m[b] * 2) % 10000 == b:
            result = 'D' + result
        elif m[b] -1 == b:
            result = 'S' + result
        elif not m[b] and b == 9999:
            result = 'S' + result
        elif (m[b] % 1000) * 10 + (m[b] // 1000) == b:
            result = 'L' + result
        elif (m[b] % 10) * 1000 + (m[b] // 10) == b:
            result = 'R' + result
        b = m[b]
    return result
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    m = [-1 for _ in range(10001)]
    print(bfs(a,b))