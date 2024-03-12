N, M, K = map(int, input().split())
# M: 증가하는 수열 크기가 군집의 개수
# K: 감소하는 수열 크기가 군집의 크기
# 군집의 개수가 군집의 크기보다 우선임.
ans = []
if N + 1 < M + K or N > M * K:
    print(-1)
    exit()

if K == 1:
    print(*list(range(1, N + 1)))
    exit()

d, r = (N - M) // (K - 1), (N - M) % (K - 1)
part_ = [K if i < d else 1 for i in range(M)]
part_[-1] += r

idx = 0
for i in part_:
    ans.extend(list(range(idx + i, idx, -1)))
    idx += i
print(*ans)