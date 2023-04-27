import sys
from collections import deque

input = sys.stdin.readline

N, M, x, y, K = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))
dice = deque([0, 0, 0, 0, 0, 0])  # N,W,B,E,S,T
dir = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}


def dice_rotate(dx, dy):
    if dx:
        dice_h = deque([dice[1], dice[2], dice[3], dice[5]])
        dice_h.rotate(dx)
        dice[1], dice[2], dice[3], dice[5] = dice_h
    if dy:
        dice_v = deque([dice[0], dice[2], dice[4], dice[5]])
        dice_v.rotate(dy)
        dice[0], dice[2], dice[4], dice[5] = dice_v


for m in move:
    dx, dy = dir[m]
    if 0 <= x + dx < N and 0 <= y + dy < M:
        x = x + dx
        y = y + dy
        dice_rotate(dx, dy)
        if grid[x][y]:
            dice[2] = grid[x][y]
            grid[x][y] = 0
        else:
            grid[x][y] = dice[2]
        print(dice[-1])
