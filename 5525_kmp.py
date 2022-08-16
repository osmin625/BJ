# IOIOI
import sys
input = sys.stdin.readline

pn = 'I' + 'OI' * int(input())
# print(pn)
m = int(input())
s = input().rstrip()
# print(s)

def kmp(s, p):
    # failure
    tb = [0 for _ in range(len(p))]
    pidx = 0
    for i in range(1, len(p)):
        while pidx and p[i] != p[pidx]:
            pidx = tb[pidx - 1]
        if p[i] == p[pidx]:
            pidx += 1
            tb[i] = pidx
    #kmp
    results = []
    pidx = 0
    for i in range(len(s)):
        while pidx and s[i] != p[pidx]:
            pidx = tb[pidx - 1]
        if s[i] == p[pidx]:
            if pidx == len(p) - 1:
                results.append(i - len(p) + 2)
                pidx = tb[pidx]
            else:
                pidx += 1
    return results
print(len(kmp(s,pn)))