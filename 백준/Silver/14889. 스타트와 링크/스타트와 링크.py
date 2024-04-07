import sys
from itertools import combinations
n = int(sys.stdin.readline())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
members = list(range(n))
min_value = sys.maxsize

for r1 in combinations(members, n//2):
    start, link = 0, 0
    r2 = list(set(members) - set(r1))
    for r in combinations(r1, 2):
        start += graph[r[0]][r[1]]
        start += graph[r[1]][r[0]]
    for r in combinations(r2, 2):
        link += graph[r[0]][r[1]]
        link += graph[r[1]][r[0]]
    min_value = min(min_value, abs(start-link))
print(min_value)