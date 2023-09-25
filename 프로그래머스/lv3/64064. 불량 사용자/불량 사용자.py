result = []
def dfs(temp,i,cases):
    if len(temp) == len(cases):
        st = sorted(temp)
        if st not in result:
            result.append(st)
        return
    for c in cases[i]:
        if c not in temp:
            temp.append(c)
            dfs(temp,i+1,cases)
            temp.pop()
    
def solution(user_id, banned_id):
    cases = [[] for _ in range(len(banned_id))]            
    for i in range(len(banned_id)):
        bid = banned_id[i]
        for uid in user_id:
            if len(uid) == len(bid):
                if all([u == b for j,u,b in zip(range(len(bid)),uid, bid) if bid[j] != '*']):
                    cases[i].append(uid)
    # print(cases)
    visited = [[0 for j in range(len(cases[i]))] for i in range(len(cases))]
    # 탐색을 위해 dfs가 필요하다.
    dfs([],0,cases)
    return len(result)