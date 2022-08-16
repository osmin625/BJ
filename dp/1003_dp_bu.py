import sys
input = sys.stdin.readline
fibo = [0,1]
for i in range(2,41):
    fibo.append(fibo[i-1] + fibo[i-2])
T = int(input())
for _ in range(T):
    N = int(input())
    if N:
        print(fibo[N-1], fibo[N])
    else:
        print(1, 0)