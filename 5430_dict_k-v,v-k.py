import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    direction = 0
    error = 0
    p = list(input().rstrip())
    n = int(input())
    temp = input()[1:-2]
    if n and ',' in temp:
        num_array = deque(map(int,temp.split(',')))
    elif n:
        num_array = deque([int(temp)])
    else:
        num_array = deque([])

    for i in p:
        if i == 'R':
            direction = abs(direction-1)
        elif num_array:
            if direction:
                num_array.pop()
            else:
                num_array.popleft()
        else:
            print('error')
            error = 1
            break
    if error:
        continue
    if direction:
        print('[',end='')
        print(*list(num_array)[::-1],sep=',',end=']\n')
    else:
        print('[', end='')
        print(*list(num_array),sep=',',end=']\n')