import sys
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)
for i in range(N):
    for j in range(1,N):
        arr[i][j] += arr[i][j-1]
for i in range(1,N):
    for j in range(N):
        arr[i][j] += arr[i-1][j]
# print(arr)
for _ in range(M):
    x1,y1,x2,y2= map(lambda x:int(x)-1,input().split())
    if x1 and y1:
        print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])
        continue
    if x1:
        print(arr[x2][y2] - arr[x1-1][y2])
        continue
    if y1:
        print(arr[x2][y2] - arr[x2][y1-1])
        continue
    print(arr[x2][y2])
