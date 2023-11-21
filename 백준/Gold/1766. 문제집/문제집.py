import sys
import heapq
input = sys.stdin.readline
N,M = map(int,input().split())

# 최대한 쉬운 문제 먼저.
# 선수 문제 존재.
# 선수 문제가 존재하는 문제를 제외한 나머지 문제들을 정렬한 후,
# 선수 문제를 빈 칸에 끼워 넣자.
# 위상 정렬 문제였다.

nums = []
graph = [[] for _ in range(N+1)]
ind = [0 for _ in range(N+1)]
queue = []

for i in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    ind[B] += 1

# 선수 문제가 없는 경우
for i in range(1,N+1):
    if not ind[i]:
        heapq.heappush(queue,i)

while queue:
    t = heapq.heappop(queue)
    nums.append(t)
    for i in graph[t]:
        ind[i] -= 1
        if not ind[i]:
            heapq.heappush(queue,i)

print(" ".join(map(str,nums)))