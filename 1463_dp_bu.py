import sys

input = sys.stdin.readline
N = int(input())
m = [i - 1 for i in range(N + 1)]
for i in range(2, N + 1):
    if i % 6 == 0:
        m[i] = min(m[i - 1], m[i // 2], m[i // 3]) + 1
    elif i % 3 == 0:
        m[i] = min(m[i - 1], m[i // 3]) + 1
    elif i % 2 == 0:
        m[i] = min(m[i - 1], m[i // 2]) + 1
    else:
        m[i] = m[i - 1] + 1
print(m[N])