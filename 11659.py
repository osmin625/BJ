import sys
input = sys.stdin.readline

N,M = map(int,input().split())
num = [0]
num.extend(list(map(int,input().split())))
for i in range(1,N+1):
    num[i] += num[i-1]
for _ in range(M):
    a,b = map(int,input().split())
    print(num[b] - num[a-1])