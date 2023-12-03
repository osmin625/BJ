import heapq
from collections import defaultdict

def solution(operations):
    max_q, min_q = [], []
    num_valid = defaultdict(int)
    def delete_one(q, i):
        nonlocal num_valid
        while q and not num_valid[i * q[0]]:
                heapq.heappop(q)
        if q:
            out = heapq.heappop(q)
            num_valid[i * out] -= 1
            return out
    
    for oper in operations:
        o, num = oper.split()
        if o == 'I':
            n = int(num)
            num_valid[n] += 1
            heapq.heappush(max_q, -n)
            heapq.heappush(min_q, n)
        elif num == '-1':
            delete_one(min_q, 1)
        else:
            delete_one(max_q, -1)
    if any(num_valid.values()):
        return [-delete_one(max_q, -1), delete_one(min_q, 1)]
    else:
        return [0,0]
        