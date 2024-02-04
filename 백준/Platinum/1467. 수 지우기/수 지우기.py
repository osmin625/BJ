import sys
from collections import Counter

input = sys.stdin.readline

num = input().rstrip()
sub = input().rstrip()
# sub의 숫자를 순서대로 뺄 필요는 없음.
# 숫자를 넣으면서 뺄 수 있을지 확인하자.
num_ = dict(Counter(num))
arr_ = dict(Counter(sub))
out = []
for n in num:
    if arr_.get(n) and num_[n] == arr_[n]:
        num_[n] -= 1
        arr_[n] -= 1
    else:
        while out:
            # n보다 큰 값이 앞에 있거나, 뺄 수 없는 숫자인 경우
            if out[-1] >= n or not arr_.get(out[-1], 0):
                break
            arr_[out[-1]] -= 1
            out.pop()
        out.append(n)
        num_[n] -= 1
print(''.join(out))