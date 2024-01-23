from sys import stdin
from heapq import heappush, heappop, heapify
N = int(input())
pq = [stdin.readline().rstrip() for _ in range(N)]
max_len_word = max(map(len,pq))
pq = list(map(lambda x:x.ljust(max_len_word,'['),pq))
idx = [0] * N
heapify(pq)
ans = []
while pq:
    word = heappop(pq)
    if word and word[0] != '[':
        word += '['
        ans.append(word[0])
        heappush(pq, word[1:])
ans = ''.join(ans)
print(ans)