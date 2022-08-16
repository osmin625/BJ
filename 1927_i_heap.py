import sys
import heapq
input = sys.stdin.readline
N = int(input())
l = []
for _ in range(N):
    x = int(input())
    if not x:
        if len(l):
            print(heapq.heappop(l))
        else:
            print(0)
    else:
        heapq.heappush(l,x)