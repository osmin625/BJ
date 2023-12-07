import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
parent = list(range(N))

def is_group(i,j):
    global lines
    def ccw(x1, y1, x2, y2, x3, y3):
        # 신발끈 공식
        a = x1 * y2 + x2 * y3 + x3 * y1
        b = x2 * y1 + x3 * y2 + x1 * y3
        return a - b
    c1 = ccw(*lines[i], *lines[j][:2])
    c2 = ccw(*lines[i], *lines[j][2:])
    c3 = ccw(*lines[i][:2], *lines[j])
    c4 = ccw(*lines[i][2:], *lines[j])
    if c1 or c2:
        if c1 * c2 <= 0 and c3 * c4 <= 0:
            return True
    else: # c1 == 0 and c2 == 0. 즉,네 점이 직선 상에 존재하는 경우
        x1, y1, x2, y2 = lines[i]
        x3, y3, x4, y4 = lines[j]
        xi, xj = (x1, x2), (x3, x4)
        yi, yj = (y1, y2), (y3, y4)
        if max(xi) >= min(xj) and max(xj) >= min(xi) \
            and max(yi) >= min(yj) and max(yj) >= min(yi):
            return True
    return False

def find_parent(i):
    if parent[i] == i:
        return i
    parent[i] = find_parent(parent[i])
    return parent[i]

def union(i, j):
    pi, pj = find_parent(i), find_parent(j)
    if pi < pj:
        parent[pj] = pi
    else:
        parent[pi] = pj
for i in range(1,N):
    for j in range(i):
        if is_group(i, j):
            union(i, j)

for i in range(N):
    parent[i] = find_parent(i)
out = Counter(parent)
print(len(out))
print(out.most_common()[0][1])