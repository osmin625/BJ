import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    c = dict()
    cnt = 1
    for _ in range(n):
        v,k = input().split()
        if k in c.keys():
            c[k].append(v)
        else:
            c[k] = [v]
    for v in c.values():
        cnt *= len(v) + 1
    print(cnt-1)