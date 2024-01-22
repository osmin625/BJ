from heapq import heappush, heappop
import sys
input = sys.stdin.readline

arr = [list(map(int,input().split())) for _ in range(int(input()))] # 거리, 연료량
L, P = map(int,input().split()) # 마을까지의 거리, # 기존 연료량
arr.append([L, 0])
arr.sort()


def solution(L, P):
    pq, cnt = [], 0
    for a, b in arr:
        if P >= L:
            return cnt
        while P < a and pq:
            P -= heappop(pq)
            cnt += 1
        if P < a:
            return -1
        heappush(pq, -b)
    return cnt


print(solution(L, P))