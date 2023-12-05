n,s = map(int,input().split())
ans = list(map(int,input().split()))
wow = []
sum_ = 0
j = 0
for i in range(n):
    sum_ += ans[i]
    if sum_ >= s:
        while sum_ >= s:
            wow.append(i-j+1)
            sum_ -= ans[j]
            j += 1
print(min(wow or [0]))