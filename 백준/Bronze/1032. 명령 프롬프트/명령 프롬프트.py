import sys
input = sys.stdin.readline

n = int(input())
pat = list(input().rstrip())
for _ in range(n-1):
    text = list(input().rstrip())
    for i in range(len(pat)):
        if pat[i] != text[i]:
            pat[i] = '?'
print(*pat,sep='')

