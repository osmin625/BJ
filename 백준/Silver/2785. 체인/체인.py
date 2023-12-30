import sys
input = sys.stdin.readline
N = int(input())

L = list(map(int,input().split()))
L.sort()
con = 0 # 연결 횟수
N -= 1
for i in L:
    if not N:
        break
    N -= 1
    con += 1
    if i <= N:
        N -= i
        con += i - 1
print(con)