import sys
input = sys.stdin.readline

N = int(input())
position = [list(map(int,input().split())) for _ in range(N)]
# print(position)
# 어? 이거 신발끈 공식?

def shoes(pos):
    return abs(sum([pos[i][0] * pos[(i + 1) % N][1] for i in range(N)]) - sum([pos[i][1] * pos[(i + 1) % N][0] for i in range(N)])) / 2
print(shoes(position))
