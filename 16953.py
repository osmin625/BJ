import sys

input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 0
while True:
    if A == B:
        print(cnt + 1)
        break
    elif A > B or B % 10 != 1 and B % 2:
        print(-1)
        break
    elif B % 10 == 1:
        B //= 10
    else:
        B //= 2
    cnt += 1
