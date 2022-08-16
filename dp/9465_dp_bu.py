import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    s = [list(map(int, input().split())), list(map(int, input().split()))]
    sum = [[0 for _ in range(n)] for _ in range(2)]
    if n == 1:
        print(max(s[0][0], s[1][0]))
    elif n == 2:
        print(max(s[0][1] + s[1][0], s[0][0] + s[1][1]))
    else:
        sum[0][0], sum[1][0] = s[0][0], s[1][0]
        sum[0][1] = s[0][1] + s[1][0]
        sum[1][1] = s[0][0] + s[1][1]
        for i in range(2,n):
            sum[0][i] = s[0][i] + max(sum[1][i-2],sum[1][i-1],sum[0][i-2] + s[1][i-1])
            sum[1][i] = s[1][i] + max(sum[0][i-2],sum[0][i-1],sum[1][i-2] + s[0][i-1])
        print(max(sum[0][n-1],sum[1][n-1]))