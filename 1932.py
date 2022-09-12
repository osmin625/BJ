import sys
input = sys.stdin.readline

n = int(input())
t = [[int(input())]]
[t.append(list(map(int,input().split()))) for _ in range(n-1)]
m = [[0 for _ in range(n)] for _ in range(n)]
# print(t)
if n == 1:
    print(t[0][0])
else:
    m[0][0] = t[0][0]
    for i in range(1,n):
        for j in range(i + 1):
            if not j:
                m[i][j] = t[i][j] + m[i-1][j]
            elif 0 < j < i:
                m[i][j] = t[i][j] + max(m[i-1][j-1],m[i-1][j])
            else:
                m[i][j] = t[i][j] + m[i-1][j-1]
    print(max(m[n-1]))