# 이웃 팀만 대여 가능
# 일부만 여분 카약 존재
# 출발 못하는 팀 수 세기

N, S, R = map(int, input().split())
break_ = [int(input())] if S == 1 else list(map(int, input().split()))
spare = [int(input())] if R == 1 else list(map(int, input().split()))

self_ = set(break_).intersection(set(spare))
S -= len(self_)
spare = {k: 1 for k in spare if k not in self_}
break_ = {k:[] for k in break_ if k not in self_}
# 관건: 한 번에 처리하기. 동일한 상황 내에서 처리하기.

for b in break_:
    if b + 1 in spare:
        break_[b].append(b + 1)
    if b - 1 in spare:
        break_[b].append(b - 1)
b_ord = sorted(break_.items(), key=lambda x:len(x[1]))
ans = S
for b, s in b_ord:
    if not s or s[0] not in spare:
        continue
    elif spare[s[0]]:
        spare[s[0]] = 0
        ans -= 1
    elif len(s) == 2:
        if s[1] not in spare:
            continue
        elif spare[s[1]]:
            spare[s[1]] = 0
            ans -= 1
print(ans)