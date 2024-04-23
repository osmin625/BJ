'''
멘토 n
상담 유형 1 ~ k
멘토 1명은 참가자 1명과 상담 가능

상담 유형 k인 참가자의 상담 멘토 고르는 방법
1. 현재 상담 중이 아닌 k 멘토
2. 모든 k 멘토가 상담 중인 경우 -> waiting
- 기다린 시간: waiting 시작 시간 ~ 상담을 시작할 때 까지의 시간
3. 멘토는 상담 끝나자마자 가장 오래 기다린 참가자와 상담 시작.

out
모든 상담자의 기다린 시간 합이 최소가 되도록 상담 유형별로 멘토 정하기.
각 유형별로 최소 멘토 1 명은 있어야 함.

solving
최적화 문제.
그리디와 dp 중 무엇일까?
그리디로 추정됨.
모르겠어서 bf로 전환.
최대 20 C 5의 경우의 수 => 15504

조합으로 가능한 배정의 경우의 수 모두 추출
각 경우의 수마다 기다린 시간 계산 후 최솟값 return
output return

'''
from heapq import heappush,heappop
from itertools import product

def wait_time(cnt, req_i):
    time = 0
    hq = []
    for t, gap in req_i:
        if len(hq) < cnt:
            heappush(hq, t + gap)
        else:
            while hq:
                end = heappop(hq)
                if end >= t:
                    time += end - t # 기다린 시간
                    heappush(hq, end + gap)
                    break
                else:
                    heappush(hq, t + gap)
                    break
    return time

def get_cases(k, n):
    if n == k:
        return [[1] * k]
    cand = [c for c in list(product(range(1, n), repeat=k)) if sum(c) == n]
    return cand

    
def solution(k, n, reqs):
    req = {i:[] for i in range(1, k + 1)}
    for t, gap, idx in reqs:
        req[idx].append((t, gap))
    min_wait_time = 1e9
    
    for cnts in get_cases(k, n):
        # print(cnts)
        wait_time_sum = 0
        for i in range(k):
            wait_time_sum += wait_time(cnts[i], req[i + 1])
        if wait_time_sum < min_wait_time:
            min_wait_time = wait_time_sum
    
    return min_wait_time