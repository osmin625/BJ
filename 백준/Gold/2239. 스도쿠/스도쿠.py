def is_promising(x,y, val):
    for i in range(9):
        if board[i][y] == val:
            return False
        if board[x][i] == val:
            return False
    # 박스
    box_x, box_y = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if board[box_x + i][box_y + j] == val:
                return False
    return True


def find_empty():
    for i in range(9):
        for j in range(9):
            if not board[i][j]:
                return True, i, j
    return False, None, None


def dfs():
    empty, x, y = find_empty()
    if not empty:
        return True
    else:
        for i in range(1, 10):
            if is_promising(x,y,i):
                board[x][y] = i
                if dfs():
                    return True
                board[x][y] = 0
        return False


board = [list(map(int,input())) for i in range(9)]
dfs()
for b in board:
    print(''.join(map(str,b)))