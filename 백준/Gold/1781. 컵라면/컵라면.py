import sys
import heapq
input = sys.stdin.readline
arr = sorted([list(map(int,input().split())) for _ in range(int(input()))])
que = []

for dead, cup in arr:
    heapq.heappush(que,cup)
    if dead < len(que):
        heapq.heappop(que)
print(sum(que))