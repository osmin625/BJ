import sys
input = sys.stdin.readline

N, M, K = map(int,input().split()) # 트랙 길이, 심판 수, pos 개수
pos = list(map(int,input().split()))

def check(gap):
    cnt, x = 0, -1
    for p in pos:
        if x <= p:
            cnt += 1
            x = p + gap
    if cnt < M:
        return False
    return True


def bisect():
    start, end = 0, pos[-1] + 1
    while start + 1 < end:
        mid = (start + end) // 2
        if check(mid):
            start = mid
        else:
            end = mid
    return start


ans = []
x, cnt = -1, 0
gap = bisect()
for p in pos:
    if x <= p and cnt < M:
        ans.append(1)
        x = p + gap
        cnt += 1
    else:
        ans.append(0)
print(''.join(map(str,ans)))