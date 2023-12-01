import sys
input = sys.stdin.readline

N,S = map(int,input().split())
nums = [0]
nums.extend(list(map(int,input().split())))
for i in range(1,N+1):
    nums[i] += nums[i-1]
# print(nums)
i, j = 0, 0
min_len = N + 1
while True:
    i += 1
    if i == N+1:
        break
    while j <= i and nums[i] - nums[j] >= S:
        min_len = min(min_len,i - j)
        j += 1
if min_len == N + 1:
    print(0)
else:
    print(min_len)
