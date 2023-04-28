import sys
input = sys.stdin.readline
from itertools import combinations

L,C = list(map(int,input().split()))
keys = input().split()
m = ['a','e','i','o','u']
ans = []
ans = list(combinations(keys,L))
ans = list(map(sorted,ans))
ans = sorted(ans)
for a in ans:
    check = len(set(a).intersection(m))
    if check and L - check >= 2:
        print(''.join(a))