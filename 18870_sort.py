import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int,input().split()))
idx = range(N)
x = list(map(list,zip(x,idx)))
x = sorted(x,key=lambda x:x[0])
n=0
x[0].append(n)
for i in range(1,N):
    if x[i][0] != x[i-1][0]:
        n+=1
    x[i].append(n)
x = sorted(x,key=lambda x:x[1])
for i in x:
    print(i[2],end=' ')