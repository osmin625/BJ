N,M = map(int,input().split())
man = [0 for _ in range(N+1)]
tman = input()
if len(tman) > 1:
    tman = list(map(int,tman.split()))
    for t in tman[1:]:
        man[t] = 1
party = [list(map(lambda x: (int(x),man[int(x)]),input().split()))[1:] for _ in range(M)]
# print(party)
for p in range(M):
    party[p] = sorted(party[p],key=lambda x:x[1],reverse=True)
party = sorted(party,key=lambda x:x[0][1],reverse=True)
cnt = 0
for part in party:
    for p in part:
        if man[p[0]]:
            for i in range(len(part)):
                man[part[i][0]] = 1
            flag = 1
    if not flag:
        cnt += 1
print(man)
print(party)
print(cnt)