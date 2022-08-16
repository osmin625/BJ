import sys
input = sys.stdin.readline
M = int(input())
S = [0]*20
for _ in range(M):
    line = input().rstrip().split()
    if len(line) > 1:
        x = int(line[1]) -1
        if line[0] == 'add':
            S[x] = 1
        elif line[0] == 'remove':
            S[x] = 0
        elif line[0] == 'check':
            print(S[x])
        elif line[0] == 'toggle':
            S[x] = 1-S[x]
    elif line[0] == 'all':
        S = [1]*20
    else:
        S = [0]*20