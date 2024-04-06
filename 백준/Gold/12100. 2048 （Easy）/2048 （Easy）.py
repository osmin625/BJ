from collections import deque
from copy import deepcopy
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

def upward(cp_grid):
    temp = [deque() for _ in range(N)]
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if cp_grid[j][i]:
                temp[i].append(cp_grid[j][i])
        temp[i].append(-1)
    for i in range(len(temp)):
        node = temp[i].popleft()
        while node != -1:
            if node and node == temp[i][0]:
                node += temp[i].popleft()
            temp[i].append(node)
            node = temp[i].popleft()
    for i in range(N):
        for j in range(len(temp[i])):
            board[j][i] = temp[i][j]
    return board


def left_(cp_grid):
    temp = deepcopy(cp_grid)
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        temp[i] = deque([t for t in temp[i] if t])
        temp[i].append(-1)
        node = temp[i].popleft()
        while node != -1:
            if node and node == temp[i][0]:
                node += temp[i].popleft()
            temp[i].append(node)
            node = temp[i].popleft()


    for i in range(N):
        for j in range(len(temp[i])):
            board[i][j] = temp[i][j]
    return board

def down_(cp_grid):
    temp = [deque() for _ in range(N)]
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N-1, -1, -1):
            if cp_grid[j][i]:
                temp[i].append(cp_grid[j][i])
        temp[i].append(-1)
    for t in temp:
        node = t.popleft()
        while node != -1:
            if node and node == t[0]:
                node += t.popleft()
            t.append(node)
            node = t.popleft()
    for i in range(N):
        for j in range(len(temp[i])):
            board[N-1-j][i] = temp[i][j]
    return board

def right_(cp_grid):
    temp = deepcopy(cp_grid)
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        temp[i] = deque([t for t in temp[i] if t])
        temp[i].appendleft(-1)
        node = temp[i].pop()
        while node != -1:
            if node and node == temp[i][-1]:
                node += temp[i].pop()
            temp[i].appendleft(node)
            node = temp[i].pop()
    for i in range(N):
        temp[i] = list(reversed(temp[i]))
        for j in range(len(temp[i])):
            board[i][N-1-j] = temp[i][j]
    return board

ans = 0
def dfs(cp_grid, depth):
    global ans
    # print(*cp_grid, sep='\n')
    # print(depth)
    if depth == 5:
        ans = max(ans, max(map(max,cp_grid)))
        return
    dfs(left_(cp_grid),depth + 1)
    dfs(upward(cp_grid), depth + 1)
    dfs(right_(cp_grid), depth + 1)
    dfs(down_(cp_grid), depth + 1)
    return ans

dfs(grid, 0)
print(ans)

# print(left_())
# print(right_())
# print(upward())
# print(down_())
