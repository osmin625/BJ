import sys


def solution():
    n, k = int(input()), int(input())
    if n <= k:
        return 0
    pos = list(map(int, sys.stdin.readline().split()))
    pos = sorted(pos)
    gap = [pos[i + 1] - pos[i] for i in range(len(pos) - 1)]
    gap.sort()
    # return sum(gap[:-(k-1)])
    return sum(gap[:len(pos) - k])


print(solution())