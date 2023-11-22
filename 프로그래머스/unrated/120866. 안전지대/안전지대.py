
def is_safe(board,i,j):
    l = len(board)
    dir = [[0,1], [0,-1],[1,1],[1,0],[1,-1],[-1,1],[-1,0],[-1,-1],[0,0]]
    return not any([board[i + dx][j + dy] for dx, dy in dir if 0 <= i + dx < l and 0 <= j + dy < l])
def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            answer += 1 if is_safe(board,i,j) else 0
    return answer