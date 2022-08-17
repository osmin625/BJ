# 1012 유기농 배추
import sys
input = sys.stdin.readline
dir = [(0,1),(0,-1),(1,0),(-1,0)]
stack = []
T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    m = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X,Y = map(int,input().split())
        m[Y][X] = 1
    # print(*m,sep=' \n')
    result = 0
    for Y in range(N):
        for X in range(M):
            if m[Y][X] == 1:
                stack.append((X,Y))
                while(stack):
                    x,y = stack.pop()
                    for dx, dy in dir:
                        a = x + dx
                        b = y + dy
                        if 0 <= a < M and 0 <= b < N and m[b][a] == 1 and (a,b) not in stack:
                            stack.append((a,b))
                    m[y][x] = 2
                result += 1
    print(result)