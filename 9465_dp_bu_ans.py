import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]
    if n > 1:
        s[0][1] += s[1][0]
        s[1][1] += s[0][0]
    for i in range(2,n):
        s[0][i] += max(s[1][i-1],s[1][i-2])
        s[1][i] += max(s[0][i-1],s[0][i-2])
    print(max(s[0][n-1],s[1][n-1]))
    # 가장 잘 푼 사람의 코드 # 기록용 # bottom-up