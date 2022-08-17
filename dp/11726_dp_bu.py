import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(1001)]
dp[0], dp[1] = 1, 1
for i in range(2,1001):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n] % 10007)