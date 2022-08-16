# 11047 동전 0
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
price = list(reversed([int(input()) for _ in range(N)]))
cnt = 0
for p in price:
    if K >= p:
        cnt += K // p
        K %= p
print(cnt)