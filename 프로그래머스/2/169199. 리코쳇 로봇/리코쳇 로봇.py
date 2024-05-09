'''
11:29~
보드게임판을 기울여서 말 움직이기
시작 위치에서 목표 위치까지 도달하는데 걸리는 최소 턴 수
말은 선택한 방향으로 막힐 때까지 움직임.
장애물이나 보드 끝에 도달하면 막힘.
일단 bfs나 dfs문제로 보임.
'''
from collections import deque

dir_ = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        
def solution(board):
    def get_distance(x, y, dx, dy):
        '''
        몇 칸이나 움직일지 계산하기
        '''
        nonlocal board, n, m
        dist = 0
        nx, ny = x, y
        while True:
            nx, ny = nx + dx, ny + dy
            if 0 <= nx < n and 0 <= ny < m\
                and board[nx][ny] != 'D':
                    dist += 1
            else:
                break
        return dist
    
    
    n, m = len(board), len(board[0])
    answer = 0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    robot, goal = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                robot = (i, j)
                visited[i][j] = 1
                break
            elif board[i][j] == 'G':
                goal = (i, j)
    q = deque([robot])
    
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if (x, y) == goal:
                return answer
            for dx, dy in dir_:
                dist = get_distance(x, y, dx, dy)
                nx, ny = x + dx * dist, y + dy * dist
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
        answer += 1
    return -1