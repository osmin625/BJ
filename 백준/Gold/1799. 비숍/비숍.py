# bishop
import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
output = []


def half_board(color):
    global board
    bo = [[board[i][j] if (i+j) % 2 == color else 0 for j in range(N)] for i in range(N)]
    return bo


def is_collision(i,j,bishops):
    for b in bishops:
        if abs(b[0] - i) == abs(b[1] - j):
            return True
    return False


def dfs(i,j, board, bishops):
    if i == N-1 and j == N:
        global output
        output.append(len(bishops))
        return
    if j == N:
        dfs(i+1, 0, board, bishops)
        return
    if board[i][j] and not is_collision(i,j,bishops):
        board[i][j] = 2
        bishops.append((i,j))
        dfs(i,j+1,board,bishops)
        board[i][j] = 1
        bishops.pop()
        dfs(i,j+1,board,bishops)
    else:
        dfs(i,j+1,board,bishops)


white = half_board(0)
dfs(0,0,white,[])
wout = max(output)

output = []
black = half_board(1)
dfs(0,0,black,[])
bout = max(output)

print(wout + bout)
