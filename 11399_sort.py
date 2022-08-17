import sys
input = sys.stdin.readline

N = int(input())
time = sorted(map(int,input().split()))
sum = 0
for i in range(N):
    sum += time[i] * (N - i)
print(sum)