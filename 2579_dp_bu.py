import sys
input = sys.stdin.readline
N = int(input())
stair = [int(input()) for _ in range(N)]
score = [0 for _ in range(N+1)]
if N < 4:
    score[0] = stair[0]
    if N == 2:
        score[1] = stair[0] + stair[1]
    if N == 3:
        score[2] = stair[2] + max(stair[0], stair[1])
    print(score[N-1])
else:
    score[0] = stair[0]
    score[1] = stair[0] + stair[1]
    score[2] = stair[2] + max(stair[0], stair[1])
    for i in range(3,N):
        score[i] = stair[i] + max(score[i-2],score[i-3] + stair[i-1])
    print(score[N-1])