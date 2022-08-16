# 7662 이중 우선순위 큐
import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    check = [0 for _ in range(k)]
    max_heap = []
    min_heap = []
    for i in range(k):
        o, n = input().split()
        n = int(n)
        if o == 'I':
            heapq.heappush(max_heap, (-n, i))
            heapq.heappush(min_heap, (n, i))
        elif o == 'D':
            if n == 1:
                while max_heap:
                    if check[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    else:
                        break
                if max_heap:
                    v, idx = heapq.heappop(max_heap)
                    check[idx] = 1
            elif n == -1:
                while min_heap:
                    if check[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                    else:
                        break
                if min_heap:
                    v, idx = heapq.heappop(min_heap)
                    check[idx] = 1
    while max_heap:
        if check[max_heap[0][1]]:
            v, idx = heapq.heappop(max_heap)
        else:
            break
    while min_heap:
        if check[min_heap[0][1]]:
            v, idx = heapq.heappop(min_heap)
        else:
            break
    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')