# 과목 마일리지 1~36
# 마일리지 많은 순으로 수강신청
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cand = []
for _ in range(n):
    P_len, L = map(int,input().split())
    P = sorted(list(map(int, input().split())),reverse=True)
    if L <= P_len:
        cand.append(P[L-1])
    else:
        cand.append(1)
    # print(P)
cand.sort()
# print(cand)
cnt = 0
for c in cand:
    if m < c:
        break
    m -= c
    cnt += 1
print(cnt)



# 못 잡는 과목은 포기해야 함.
# 현재의 최선을 구하는 방법
# 가장 적은 마일리지로 잡을 수 있는 과목 정렬.
