# 1074 Z
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N, r, c = map(int, input().split())
num = 2 ** (2 * N - 2)
z = 2 ** (N - 1)
result=0
def cal(rstart, cstart, z,num,result):
    # print(rstart,cstart,result,z)
    if not z:
        print(result)
    elif r < rstart + z and c < cstart + z:
        result += num * 0
        cal(rstart, cstart, z // 2,num//4,result)
    elif r < rstart + z and cstart + z <= c:
        result += num * 1
        cal(rstart, cstart + z, z // 2,num//4,result)
    elif rstart + z <= r and c < cstart + z:
        result += num * 2
        cal(rstart + z, cstart, z // 2,num//4,result)
    elif rstart + z <= r and cstart + z <= c:
        result += num * 3
        cal(rstart + z, cstart + z, z // 2,num//4,result)

cal(0, 0, z,num,result)