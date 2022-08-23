import sys

input = sys.stdin.readline
dp = [0 for _ in range(50001)]
sq = [i*i for i in range(224)]
n = int(input())
if n in sq:
    print(1)
else:
    for i in range(1, n+1):
        if i in sq:
            dp[i] = 1
        else:
            t = []
            j = 1
            while j * j <= i:
                t.append(dp[j * j] + dp[i - j * j])
                j += 1
            dp[i] = min(t)
    print(dp[n])
