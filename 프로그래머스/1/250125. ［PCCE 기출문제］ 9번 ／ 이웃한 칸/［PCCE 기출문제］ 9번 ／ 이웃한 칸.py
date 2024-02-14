def solution(board, h, w):
    answer = 0
    dir_ = {(1,0),(-1,0),(0,1),(0,-1)}
    n = len(board)
    for dh, dw in dir_:
        if 0 <= h + dh < n and 0 <= w + dw < n:
            if board[h + dh][w + dw] == board[h][w]:
                answer += 1
    return answer