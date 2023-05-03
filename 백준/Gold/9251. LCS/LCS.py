import sys
from itertools import combinations
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())
# print(s1,s2)
l1 = len(s1)
l2 = len(s2)

m = [0 for _ in range(l2)]
for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < m[j]:
            cnt = m[j]
        elif s1[i] == s2[j]:
            m[j] = cnt + 1
    # print(s1[i],m)
print(max(m))