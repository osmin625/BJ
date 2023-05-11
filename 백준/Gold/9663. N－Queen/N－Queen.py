N = int(input())
queen = [0 for _ in range(N)]
ans = 0


def is_promising(x):
    for i in range(x):
        if queen[i] == queen[x] or abs(queen[i]-queen[x]) == x-i:
            return 0
    else:
        return 1


def dfs(x):
    global ans
    if x == N:
        ans += 1
        return
    for i in range(N):
        queen[x] = i
        if is_promising(x):
            dfs(x+1)


dfs(0)
print(ans)