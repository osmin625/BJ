import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, S = input().rstrip().split()
    R = int(R)
    S = list(S)
    for s in S:
        print(s * R,end='')
    print()