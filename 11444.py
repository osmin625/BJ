import sys
sys.setrecursionlimit(10**7)
n = int(input())


def dc(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        t1 = dc(n // 2)
        t2 = dc(n // 2 - 1)
        return (t1 ** 2 + t2 ** 2 + t1 * t2) % 1000000007
print(dc(n))
