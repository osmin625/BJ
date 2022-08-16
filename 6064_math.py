# 카잉 달력
import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    # print(M, N, x, y)
    max = lcm(M, N)
    a, b = x, y
    flag = 0
    while a <= max and b <= max:
        if a < b:
            a += M
        elif a > b:
            b += N
        else:
            flag = 1
            print(a)
            break
    if not flag:
        print(-1)