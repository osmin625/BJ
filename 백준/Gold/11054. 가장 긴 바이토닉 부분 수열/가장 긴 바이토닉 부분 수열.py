import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
asc = [1 for _ in range(N)]
desc = [1 for _ in range(N)]
m = 0
for i in range(1,N):
    for j in range(i):
        if A[j] < A[i]:
            asc[i] = max(asc[i],asc[j] + 1)
for i in range(N-2,-1,-1):
    for j in range(N-1,i,-1):
        if A[j] < A[i]:
            desc[i] = max(desc[i],desc[j] + 1)
# print(asc)
# print(desc)
print(max([x+y-1 for x,y in zip(asc,desc)]))
