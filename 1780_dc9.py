import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
N = int(input())
size = N
sx = sy = 0
m = [list(map(int, input().split())) for _ in range(N)]
# print(*m, sep='\n')
cnt = [0, 0, 0]


def dc(sx, sy, size):
    flag = 0
    v = m[sx][sy]
    for x in range(sx, sx + size):
        for y in range(sy, sy + size):
            if v != m[x][y]:
                flag = 1
                break
        if flag:
            break
    if flag and size > 1:
        s = size // 3
        dc(sx        , sy        , s)
        dc(sx        , sy + s    , s)
        dc(sx        , sy + s * 2, s)

        dc(sx + s    , sy        , s)
        dc(sx + s    , sy + s    , s)
        dc(sx + s    , sy + s * 2, s)

        dc(sx + s * 2, sy        , s)
        dc(sx + s * 2, sy + s    , s)
        dc(sx + s * 2, sy + s * 2, s)
    else:
        cnt[v] += 1
dc(sx, sy, size)

print(cnt[-1])
print(cnt[0])
print(cnt[1])