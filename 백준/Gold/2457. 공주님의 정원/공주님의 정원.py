import sys
input = sys.stdin.readline
n = int(input())
flower = []
for i in range(n):
    temp = tuple(map(int,input().split()))
    if temp[0] < 12:
        flower.append(temp)
flower.sort()

def solution():
    left, right = (3, 1), (3, 1)
    cnt = 0
    if (3, 1) < flower[0][:2]:
        return 0
    for f in flower:
        if left < f[:2] and left != right:
            cnt += 1
            left = right
            if left < f[:2]:
                break
        if right < f[2:]:
            right = f[2:]
    if right < (11, 31):
        return 0
    elif left < (11, 31):
        cnt += 1
    return cnt

print(solution())