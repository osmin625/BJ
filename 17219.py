import sys
input = sys.stdin.readline
d = dict()
N,M = map(int,input().split())
for _ in range(N):
    addr, pw = input().rstrip().split(' ')
    d[addr] = pw
for _ in range(M):
    find_addr = input().rstrip()
    print(d[find_addr])