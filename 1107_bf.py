import sys
input = sys.stdin.readline
N = input().rstrip()
M = int(input())
unum = dnum = int(N)
check = dcnt = ucnt = 0
current = 100
if 0 < M < 10:
    breakdown = set(map(int, input().split()))
    # print(breakdown)
    while True:
        if set(map(int, str(dnum))).intersection(breakdown) != set() and dnum > 0:
            dnum -= 1
            dcnt += 1
        elif set(map(int, str(dnum))).intersection(breakdown) == set():
            break
        if set(map(int, str(unum))).intersection(breakdown) != set():
            unum += 1
            ucnt += 1
        else:
            check = 1
            break
    if check:
        print(min(abs(int(N) - current), ucnt + len(str(unum))))
    else:
        print(min(abs(int(N) - current), dcnt + len(str(dnum))))
elif M == 10:
    input()
    print(abs(int(N) - current))
else:
    print(min(abs(int(N)-current),len(str(N))))