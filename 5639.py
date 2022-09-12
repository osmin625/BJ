import sys

sys.setrecursionlimit(10 ** 6)
num = []
while True:
    try:
        num.append(int(input()))
    except:
        break

def postorder(first, end):
    if first > end:
        return
    mid = end + 1  # 루트보다 큰 값이 존재하지 않을 경우를 대비
    for i in range(first + 1, end + 1):
        if num[first] < num[i]:
            mid = i
            break
    postorder(first + 1, mid - 1)
    postorder(mid, end)
    print(num[first])

postorder(0, len(num) - 1)