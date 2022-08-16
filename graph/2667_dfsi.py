import sys
input = sys.stdin.readline

N = int(input())
m = []
stack = []
block = 0
block_size = []
dir =[(0,1),(1,0),(0,-1),(-1,0)]
for i in range(N):
    m.append(list(map(int,input().strip())))
# print(m)
for i in range(N):
    for j in range(N):
        if m[i][j] == 1:
            apart = 0
            stack.append((i,j))
            while stack:
                a,b = stack.pop()
                for dx, dy in dir:
                    if a + dx < 0 or a + dx > N-1 or b + dy < 0 or b + dy > N-1:
                        continue
                    elif m[a + dx][b + dy] == 1 and (a + dx,b + dy) not in stack:
                        stack.append((a + dx,b+dy))
                m[a][b] = 2
                apart += 1
                # print(stack,apart)
            block += 1
            block_size.append(apart)
print(block)
for bs in sorted(block_size):
    print(bs)