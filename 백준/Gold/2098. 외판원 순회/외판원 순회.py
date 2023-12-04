# 외판원 순회
# 최소 비용 한붓 그리기
# w가 0이면 갈 수 없는 경우
# dp + 그래프 탐색
import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

dp = [defaultdict(int) for _ in range(N)]
# 순회이기 때문에 출발점은 상관 없음. 0으로 지정.
def dfs(cur, visited): # cur : current
    global dp
    if visited == (1 << N) - 1:
        if W[cur][0]:
            return W[cur][0]
        return float('inf')

    if dp[cur][visited]:
        return dp[cur][visited]

    cost = float('inf')
    for n in range(1,N): # n: next
        if W[cur][n] and not visited & (1 << n):
            cost = min(dfs(n, visited | 1 << n) + W[cur][n], cost)
    dp[cur][visited] = cost
    return cost
print(dfs(0, 1))