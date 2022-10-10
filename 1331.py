import sys
input = sys.stdin.readline
path = [list(input().rstrip()) for _ in range(36)]
move = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
visited = [[0 for _ in range(6)] for _ in range(6)]
visited[ord(path[0][0])-65][int(path[0][1])-1] = 1
flag = 0
for i in range(1,36):
    if (ord(path[i][0])-ord(path[i-1][0]),int(path[i][1])-int(path[i-1][1])) not in move:
        flag = 1
        break
    else:
        visited[ord(path[i][0])-65][int(path[i][1])-1] = 1
if (ord(path[0][0])-ord(path[35][0]),int(path[0][1])-int(path[35][1])) not in move:
    flag = 1
for i in range(6):
    if not all(visited[i]):
        flag = 1
        break
if not flag:
    print('Valid')
else:
    print('Invalid')