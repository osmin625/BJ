import sys
import bisect
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int,input().split()))

for i in range(n):
    temp = A[i]
    for j in range(i + 1, n):
        temp += A[j]
        A.append(temp)
for i in range(m):
    temp = B[i]
    for j in range(i + 1, m):
        temp += B[j]
        B.append(temp)
B.sort()
ans = 0
for a in sorted(A):
    left = bisect.bisect_left(B, T-a)
    right = bisect.bisect_right(B, T-a)
    ans += right - left
print(ans)