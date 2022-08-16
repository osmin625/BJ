import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
pic = [list(map(int,list(input().rstrip()))) for _ in range(N)]
result = ''


def dc(x, y, size):
    global result
    check = pic[x][y]
    if size == 1:
        result += str(pic[x][y])
        return
    flag = 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            if check != pic[i][j]:
                result += '('
                flag = 1
                if size >= 2:
                    size //= 2
                for ii in range(x, x + size * 2, size):
                    for jj in range(y, y + size * 2, size):
                        dc(ii,jj,size)
                result += ')'
                break
        if flag:
            break
    if not flag:
        result += str(check)
if all([all(pic[i]) for i in range(N)]):
    print(1)
elif all([all(list(map(lambda x: not x, pic[i]))) for i in range(N)]):
    print(0)
else:
    dc(0,0,N)
    print(result)