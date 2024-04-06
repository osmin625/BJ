from collections import deque
N = int(input())
K = int(input())

apple = dict()
for _ in range(K):
    t = tuple(map(int, input().split()))
    apple[t] = 1
L = int(input())

# x초 후 c 방향으로 회전
move = dict()
for _ in range(L):
    a, b = input().split()
    move[int(a)] = b

dir_ = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
turn_ = dict()
turn_['D'] = {'R': 'D', 'D': 'L', 'L': 'U', 'U': 'R'}
turn_['L'] = {'D': 'R', 'R': 'U', 'U': 'L', 'L': 'D'}

grid = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
sec = 0
px, py = 1, 1 # 머리
tail = deque([(1, 1)])
grid[1][1] = 1
d = 'R'
while True:
    # print(sec)
    # print(*grid, sep='\n')
    if move.get(sec, False): # 방향 전환
        d = turn_[move.get(sec)][d]
    sec += 1
    px += dir_[d][0]
    py += dir_[d][1]
    if 0 < px <= N and 0 < py <= N: # 벽 아닌 경우
        if grid[px][py]: # 몸통 부딪침
            break
        grid[px][py] = 1 # 머리 추가
        tail.append((px, py))  # 기록 추가
        if not apple.get((px, py), 0): # 사과 없으면
            tx, ty = tail.popleft() # 꼬리 삭제
            grid[tx][ty] = 0
        else: # 사과 없애기
            apple.pop((px, py))
    else: # 벽인 경우
        break
print(sec)
