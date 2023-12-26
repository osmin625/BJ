import sys
input = sys.stdin.readline

N = int(input())
expect_ = [int(input()) for i in range(N)]
real = sorted(enumerate(expect_),key=lambda x:x[1])
out = [0 for _ in range(N)]
for i in range(len(real)):
    out[real[i][0]] = i + 1
print(sum([abs(i-j) for i,j in zip(out,expect_)]))
