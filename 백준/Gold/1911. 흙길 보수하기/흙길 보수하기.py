import sys
import math
input = sys.stdin.readline

N, L = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(N)]
pos.sort()
ans, covered = 0, 0
for i in range(N):
    if covered >= pos[i][1]:
        continue
    elif pos[i][0] < covered:
        pos[i][0] = covered
    cnt = math.ceil((pos[i][1] - pos[i][0]) / L)
    covered = pos[i][0] + cnt * L
    ans += cnt
print(ans)