# 1, 2, 3 더하기
import sys
input = sys.stdin.readline

T = int(input())
def ott(n):
    if n==1:
        return {'1'}
    elif n == 2:
        return {'11','2'}
    elif n==3:
        return {'111','12','21','3'}
    else:
        temp = set()
        pott = ott(n-1)
        for p in range(1,4):
            for i in ott(n-p):
                temp.add(str(p)+i)
                temp.add(i+str(p))
        return temp
for _ in range(T):
    n = int(input())
    print(len(ott(n)))