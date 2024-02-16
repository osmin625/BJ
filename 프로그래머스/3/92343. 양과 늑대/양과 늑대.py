# 10분 -- bestfs
# 트리 만들기 o
# 양 큐, 늑대 큐 만들기 o
# 양 큐 먼저 탐색하기
def solution(info, edges):
    answer = 0
    tree = {i:[] for i in range(18)}
    for a, b in edges:
        tree[a].append(b)
    def dfs(start, wolf, sheep, candidates):
        nonlocal answer, info, tree
        if not info[start]:
            sheep += 1
        else:
            wolf += 1
        if wolf >= sheep:
            return
        answer = max(answer, sheep)

        for c in candidates:
            next_ = [nc for nc in candidates if nc != c]
            next_.extend(tree[c])
            dfs(c, wolf, sheep, next_)
        return
    dfs(0, 0, 0, tree[0])
    return answer