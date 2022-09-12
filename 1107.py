import sys
from itertools import permutations
from itertools import combinations

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    dots = [list(map(int, input().split())) for _ in range(N)]
    vec = list(combinations(dots, N // 2))
    total = [0, 0]
    v_sum = []
    for d in dots:
        total[0] += d[0]
        total[1] += d[1]
    # print(total)
    for vector in vec[:int(len(vec) / 2)]:
        t_sum = [0, 0]
        for v in vector:
            t_sum[0] += v[0]
            t_sum[1] += v[1]
        v_sum.append(t_sum)
    # print(v_sum)
    print(min(list(map(lambda x: ((total[0] - 2 * x[0]) ** 2 + (total[1] - 2 * x[1]) ** 2) ** 0.5, v_sum))))
