import sys

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[i + 1, *arr[i]] for i in range(N)]

# print(arr)
ans = []
dir_ = {i: [] for i in 'UDLR'}


def move(d1, d2, t):
    for r, l in enumerate(arr):
        r = r + 1
        i, a, b = l
        if r > l[t]:
            dir_[d1].extend([[i, d1, a, b]] * (r - l[t]))
        elif r < l[t]:
            dir_[d2].extend([[i, d2, a, b]] * (l[t] - r))


arr.sort(key=lambda x: x[1])
move('D', 'U', 1)
arr.sort(key=lambda x: x[2])
move('R', 'L', 2)
for d in dir_:
    if d in 'DR':
        ans.extend(reversed(dir_[d]))
    else:
        ans.extend(dir_[d])
print(len(ans))
for a in ans:
    print(a[0], a[1])