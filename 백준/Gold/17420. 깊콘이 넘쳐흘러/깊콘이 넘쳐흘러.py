import sys
import math

input = sys.stdin.readline
N = int(input())

A = list(map(int, input().split()))  # 남은 기간
B = list(map(int, input().split()))  # 계획일

AB = sorted(zip(A, B), key=lambda x: (x[1], x[0]))
a_, b_ = AB[0]
cnt = 0
for i, (a, b) in enumerate(AB):
    if a < b_:
        temp = math.ceil((b_ - a) / 30)
        cnt += temp
        a += temp * 30
        AB[i] = (b, a)
    a_ = max(a, a_)
    if i + 1 < N and AB[i + 1][1] != b:
        b_ = max(a_, AB[i + 1][1])
print(cnt)