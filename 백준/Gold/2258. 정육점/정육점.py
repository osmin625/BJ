import sys

input = sys.stdin.readline


def output():
    N, M = map(int, input().split())
    items_ = [list(map(int, input().split())) for _ in range(N)]
    items_.sort(key=lambda x: (x[1], -x[0]))
    # print(items_)
    ans = []
    cost = items_[0][1]
    for i in range(1, N):
        if cost == items_[i][1]:  # 가격이 동일한 경우
            items_[i][1] += items_[i - 1][1]  # 가격 누적
        else:
            cost = items_[i][1]
        items_[i][0] += items_[i - 1][0]  # 무게 누적
        if items_[i][0] >= M:
            ans.append(items_[i][1])
    if ans:
        ans.sort()
        return ans[0]
    else:
        return -1

print(output())
