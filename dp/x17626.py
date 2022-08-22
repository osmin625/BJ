import sys
input = sys.stdin.readline
sq = list(reversed([i * i for i in range(1,224)]))
m = [0 for _ in range(50001)]
def dp(n):
    if n in sq:
        return 1
    for i in range(224):
        if n > s[i]:
            return
    return m[n]
print(dp(int(input())))