import sys

input = sys.stdin.readline

N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def mul(a, b):
    t = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                t[i][j] += a[i][k] * b[k][j]
    return t


def dc(N, B):
    if B == 1:
        return [list(map(lambda x: x % 1000, arr[i])) for i in range(N)]
    else:
        d = dc(N, B // 2)
        if B % 2:
            return [list(map(lambda x: x % 1000, mul(mul(d, d), arr)[i])) for i in range(N)]
        else:
            return [list(map(lambda x: x % 1000, mul(d, d)[i])) for i in range(N)]


result = dc(N, B)
[print(*result[_], sep=' ') for _ in range(N)]
