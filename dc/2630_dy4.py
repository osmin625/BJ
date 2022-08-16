# 색종이 만들기
import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]
# print(*grid,sep='\n')
paper = [0,0]
def dc(x,y,n):
    check = grid[x][y]
    if n == 1:
        paper[check] += 1
        return
    flag = 0
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != grid[i][j]:
                flag = 1
                for ii in range(x,x+n,n//2):
                    for jj in range(y,y+n,n//2):
                        dc(ii,jj,n//2)
                break
        if flag:
            break
    if not flag:
        paper[check] += 1
dc(0,0,N)
print(*paper,sep='\n')