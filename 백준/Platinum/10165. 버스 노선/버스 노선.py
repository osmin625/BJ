import heapq
import sys
input = sys.stdin.readline
# 출발 순 삽입, 끝 순 삭제
# 만약 시작 지점이 되돌아온 경우: heap의 처음부터 검사하여 끝 지점을 통과하면 삭제.
q = []
N, M = int(input()), int(input())
lines = []
for i in range(M):
    start, end = list(map(int, input().split()))
    if start > end:
        end += N
    lines.append([start, end, i + 1])
lines.sort(key=lambda x:[x[0], -x[1]])
qEnd = 0
for line in lines:
    if not q:
        q = [line]
        qEnd = line[1]
    else:
        if line[1] > qEnd:
            heapq.heappush(q, line)
            qEnd = line[1]
        if line[1] >= N:
            while q[0][1] <= line[1] - N:
                # print('hello', q[0], line)
                heapq.heappop(q)
    # print('q:', q)
print(*sorted([i for _, _, i in q]))